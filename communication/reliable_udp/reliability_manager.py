import logging
import time
from collections import namedtuple
from threading import RLock, Thread

from common.generic_event import GenericEvent
from common.time_utils import TimeUtils
from communication.reliable_udp.partition import Partition
from logging_provider.logging_initiator import LoggingInitiator

logger = logging.getLogger(LoggingInitiator.MAIN_LOGGER)
MessageIdEventArgs = namedtuple('MessageIdEventArgs', ['message_id'])
PartitionEventArgs = namedtuple('PartitionEventArgs', ['partition'])

class ReliabilityManager:
    def __init__(self, ack_check_interval: float, part_timeout_interval):
        if ack_check_interval > part_timeout_interval:
            raise Exception("ack_check_interval can't be larger then part_timeout_interval")
        self._ack_check_interval = ack_check_interval
        self._part_timeout_interval = part_timeout_interval
        self._send_partitions_dict: dict[int, list[Partition]] = {}
        self.on_resend_required = GenericEvent(args_type=PartitionEventArgs)
        self.on_sent_successfully = GenericEvent(args_type=MessageIdEventArgs)
        self.on_sent_failed = GenericEvent(args_type=MessageIdEventArgs)
        self._is_ack_timeout_check_continue = True
        self._send_partitions_dict_lock = RLock()
        self._timeout_thread = Thread(target=self._ack_timeout_thread_start, name='reliability timeout thread')

    def start(self):
        logger.debug(f'reliability manager started')
        self._timeout_thread.start()

    def stop(self):
        self._is_ack_timeout_check_continue = False

    def add_message_partitions(self, message_id, partitions: list[Partition]):
        with self._send_partitions_dict_lock:
            self._send_partitions_dict[message_id] = partitions

    def _ack_timeout_thread_start(self):
        while self._is_ack_timeout_check_continue:
            time.sleep(self._ack_check_interval)
            self._check_resend_for_messages()

    def _check_resend_for_messages(self):
        """iterate all messages and check for partition resend timeout"""
        with self._send_partitions_dict_lock:
            messages_ids_to_delete = []
            for message_id in self._send_partitions_dict:
                is_need_to_delete_message = self._check_resend_for_one_message(message_id)
                if is_need_to_delete_message:
                    messages_ids_to_delete.append(message_id)
            # delete failed and empty messages
            for message_id in messages_ids_to_delete:
                logger.warning(f'message: {message_id} removed from resend dict')
                self._send_partitions_dict.pop(message_id)
                self.on_sent_failed.raise_event(MessageIdEventArgs(message_id))

    def _check_resend_for_one_message(self, message_id: int) -> bool:
        """
        iterate message partitions and check for resend timeout
        @param message_id:
        @return: true, if message need to be removed
        """
        with self._send_partitions_dict_lock:
            message_parts = self._send_partitions_dict[message_id]
            parts_to_delete = []
            for partition in message_parts:
                is_no_resends = self._check_resend_for_part(partition)
                if is_no_resends:
                    parts_to_delete.append(partition)
            for part in parts_to_delete:
                message_parts.remove(part)
            if not message_parts:
                return True  # all parts received ack or timeout and no resend left
            return False

    def _check_resend_for_part(self, partition: Partition) -> int:
        """
        check if partition has resend timeout to send again
        @param partition:
        @return: is resends left
        """
        if TimeUtils.utc_timestamp() - partition.sent_time > self._part_timeout_interval:
            if partition.resend_counter > 0:
                partition.resend_counter -= 1
                partition.sent_time = TimeUtils.utc_timestamp()
                logger.warning(
                    f'resend required for message: {partition.message_id} partition: {partition.part_number} '
                    f'nResends={partition.resend_counter} ack timeout ')
                self.on_resend_required.raise_event(PartitionEventArgs(partition=partition))
        return partition.resend_counter <= 0

if __name__ == '__main__':
    LoggingInitiator()
    rm = ReliabilityManager(0.1, 0.2)
    parts = [Partition(1000, 0, 2, b'123', '127.0.0.1', 1002, 0, 4),
             Partition(1000, 1, 2, b'123', '127.0.0.1', 1002, 1, 2)]
    rm.add_message_partitions(1000, parts)
    logger.debug(rm._send_partitions_dict)
    for _ in range(8):
        time.sleep(0.5)
        rm._check_resend_for_messages()
        logger.debug(rm._send_partitions_dict)

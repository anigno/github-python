import time
from threading import RLock, Thread

from common.generic_event import GenericEvent
from common.time_utils import TimeUtils
from communication.reliable_udp.partition import Partition

class ReliabilityManager:
    def __init__(self, ack_check_interval: float, part_timeout_interval):
        if ack_check_interval > part_timeout_interval:
            raise Exception("ack_check_interval can't be larger then part_timeout_interval")
        self.ack_check_interval = ack_check_interval
        self.part_timeout_interval = part_timeout_interval
        self.send_partitions_dict: dict[int, list[Partition]] = {}
        self.on_resend_required = GenericEvent()
        self.is_ack_timeout_check_continue = True
        self.send_partitions_dict_lock = RLock()
        self.timeout_thread = Thread(target=self.ack_timeout_thread_start)

    def start(self):
        self.timeout_thread.start()

    def stop(self):
        self.is_ack_timeout_check_continue = False

    def add_message_partitions(self, message_id, partitions: list[Partition]):
        with self.send_partitions_dict_lock:
            self.send_partitions_dict[message_id] = partitions
            self.check_resend_for_message(message_id)

    def ack_timeout_thread_start(self):
        while self.is_ack_timeout_check_continue:
            time.sleep(self.ack_check_interval)
            self.check_resend_for_messages()

    def check_resend_for_messages(self):
        with self.send_partitions_dict_lock:
            for message_id in self.send_partitions_dict:
                self.check_resend_for_message(message_id)

    def check_resend_for_message(self, message_id) -> bool:
        with self.send_partitions_dict_lock:
            for part in self.send_partitions_dict[message_id]:
                self.check_resend_for_part(part)

    def check_resend_for_part(self, part) -> bool:
        if TimeUtils.utc_timestamp() - part.sent_time > self.part_timeout_interval:
            if part.resend_counter > 0:
                part.sent_time = TimeUtils.utc_timestamp()
                self.on_resend_required.raise_event(part)
                return True
            else:
                return False

if __name__ == '__main__':
    l = [[1], [2], [3], [4], [2], [3]]
    for i, a in enumerate(l):
        if a == [2]:
            del (l[i])
            # l.remove([2])
            break
    for i, a in enumerate(l):
        print(i, a)

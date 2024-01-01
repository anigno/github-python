import logging
import time
from threading import Thread

from common.time_utils import TimeUtils
from communication.reliable_udp.partition_manager import PartitionManager
from communication.reliable_udp.reliability_manager import PartitionEventArgs, ReliabilityManager
from communication.reliable_udp.reliable_communicator_config import ReliableCommunicatorConfig
from communication.reliable_udp.unique_id_provider import UniqueIdProvider
from communication.udp.udp_communicator import UdpCommunicator
from communication.udp.event_args.data_received_event_args import DataReceivedEventArgs
from logging_provider.logging_initiator_by_code import LoggingInitiatorByCode

logger = logging.getLogger(LoggingInitiatorByCode.FILE_SYSTEM_LOGGER)

class ReliableCommunicator:

    def __init__(self, config: ReliableCommunicatorConfig, partition_manager: PartitionManager,
                 reliability_manager: ReliabilityManager):
        self.config: ReliableCommunicatorConfig = config
        self.partition_manager = partition_manager
        self.reliability_manager = reliability_manager
        self.udp_communicator = UdpCommunicator(self.config.local_ip, self.config.local_port,
                                                self.config.receive_buffer_size)
        self.reliability_manager.on_resend_required += self.on_reliability_manager_resend_required
        self.udp_communicator.on_data_received += self.on_udp_communicator_data_received

    def start_receiving(self) -> Thread:
        thread = self.udp_communicator.start_receiving()
        return thread

    def stop_receiving(self):
        self.udp_communicator.stop_receiving()

    def on_udp_communicator_data_received(self, event_args: DataReceivedEventArgs):
        pass

    def on_reliability_manager_resend_required(self, args: PartitionEventArgs):
        logger.debug(f'resend requested for {args}')
        self.udp_communicator.send_to(args.partition.target_ip, args.partition.target_port,
                                      args.partition.part_data_bytes)

    def send_to(self, target_ip: str, target_port: int, data_bytes: bytes):
        message_id = UniqueIdProvider.get_unique_message_id()
        partitions = self.partition_manager.create_partitions(data_bytes, message_id, target_ip, target_port)
        for partition in partitions:
            partition.sent_time = TimeUtils.utc_timestamp()
            self.udp_communicator.send_to(target_ip, target_port, partition.part_data_bytes)
        self.reliability_manager.add_message_partitions(message_id, partitions)
        logger.debug(f'message partitions sent: mid={message_id} [{target_ip} {target_port}] nParts={len(partitions)}')

if __name__ == '__main__':
    LoggingInitiatorByCode()  # should be called once per application
    config1 = ReliableCommunicatorConfig('127.0.0.1', 1001)
    pm = PartitionManager(5, 2)
    rm = ReliabilityManager(2, 4)
    rm.start()
    rc = ReliableCommunicator(config1, pm, rm)
    rc.start_receiving()
    rc.send_to('127.0.0.1', 1002, b'1234567890')

    for _ in range(300):
        time.sleep(0.1)
    print("\nend\n")

    # rc.stop_receiving()
    rm.stop()

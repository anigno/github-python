import logging

from common.time_utils import TimeUtils
from communication.reliable_udp.partition import Partition
from communication.reliable_udp.partition_manager import PartitionManager
from communication.reliable_udp.reliability_manager import ReliabilityManager
from communication.reliable_udp.reliable_communicator_config import ReliableCommunicatorConfig
from communication.reliable_udp.unique_id_provider import UniqueIdProvider
from communication.udp_communicator import UdpCommunicator
from logging_provider.logging_initiator import LoggingInitiator

class ReliableCommunicator:
    logger = logging.getLogger(LoggingInitiator.MAIN_LOGGER)

    def __init__(self, config: ReliableCommunicatorConfig, partition_manager: PartitionManager,
                 reliability_manager: ReliabilityManager):
        ReliableCommunicator.logger.info(f'init ReliableCommunicator with config: {config}')
        self.config: ReliableCommunicatorConfig = config
        self.partition_manager = partition_manager
        self.reliability_manager = reliability_manager
        self.udp_communicator = UdpCommunicator(self.config.local_ip, self.config.local_port,
                                                self.config.receive_buffer_size)
        self.reliability_manager.on_resend_required += self.on_reliability_manager_resend_required
        self.udp_communicator.on_data_received += self.on_udp_communicator_data_received

    def start_receiving(self):
        self.udp_communicator.start_receiving()

    def on_udp_communicator_data_received(self):
        pass

    def on_reliability_manager_resend_required(self, partition: Partition):
        pass

    def send_to(self, target_ip: str, target_port: int, data_bytes: bytes):
        message_id = UniqueIdProvider.get_unique_message_id()
        partitions = self.partition_manager.create_partitions(data_bytes, message_id, target_ip, target_port)
        for partition in partitions:
            partition.sent_time = TimeUtils.utc_timestamp()
            self.udp_communicator.send_to(target_ip, target_port, partition.part_data_bytes)
        self.reliability_manager.add_message_partitions(message_id, partitions)

if __name__ == '__main__':
    LoggingInitiator()  # should be called once per application
    config1 = ReliableCommunicatorConfig('127.0.0.1', 1000)
    pm = PartitionManager(5, 2)
    rm = ReliabilityManager(2, 4)
    rm = ReliableCommunicator(config1, pm, rm)

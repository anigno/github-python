from communication.reliable_udp.partition import Partition
from communication.reliable_udp.partition_manager import PartitionHelper, PartitionManager
from communication.reliable_udp.reliability_manager import ReliabilityManager
from communication.reliable_udp.reliable_communicator_config import ReliableCommunicatorConfig
from communication.reliable_udp.unique_id_provider import UniqueIdProvider
from communication.udp_communicator import UdpCommunicator

class ReliableCommunicator:

    def __init__(self, config: ReliableCommunicatorConfig, partition_manager: PartitionManager,
                 reliability_manager: ReliabilityManager):
        self.config: ReliableCommunicatorConfig = config
        self.partition_manager = partition_manager
        self.reliability_manager = reliability_manager

    def _init_udp_communicator(self):
        self.udp_communicator = UdpCommunicator(self.config.local_ip, self.config.local_port,
                                                self.config.receive_buffer_size)
        self.udp_communicator.on_data_received += self.on_udp_communicator_data_received
        self.udp_communicator.start_receiving()

    def on_udp_communicator_data_received(self):
        pass

    def send_to(self, target_ip: str, target_port: int, data_bytes: bytes):
        message_id = UniqueIdProvider.get_unique_message_id()
        partitions = self.partition_manager.create_partitions(data_bytes, message_id, target_ip, target_port)
        
        self.udp_communicator.send_to(target_ip, target_port, partition.data_bytes)

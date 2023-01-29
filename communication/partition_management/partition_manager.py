from typing import Dict, List

from common.generic_event import GenericEvent
from communication.partition_management.Partition import Partition

class PartitionManager:
    """
        handle the receiving of message data bytes parts to a completed message
    """

    def __init__(self, max_data_size=1024, old_data_clean_interval_sec=3.0):
        """
        ctor
        :param max_data_size: max size of each partitioned data part
        :param old_data_clean_interval_sec: when does a partitioned data part considered old and should be removed
        """
        self.old_data_clean_interval_sec = old_data_clean_interval_sec
        self.max_data_size = max_data_size
        self.on_all_parts_received = GenericEvent('on_all_parts_received')
        self.received_parts: Dict[int, List[bytes]] = {}

    def get_data_parts(self, data_bytes: bytes) -> List[Partition]:
        ret = []
        for index, cnt in enumerate(range(0, len(data_bytes), self.max_data_size)):
            partition = Partition(index, data_bytes[cnt:cnt + self.max_data_size])
            ret.append(partition)
        return ret

    def add_received_part(self, data_bytes, descriptor, index):
        pass

if __name__ == '__main__':
    pm = PartitionManager(6, 300)
    parts = pm.get_data_parts(b'01234567890123456789')
    print(parts)

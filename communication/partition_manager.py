from typing import List

class Partition:
    def __init__(self, index: int, data_bytes: bytes,receive_timeout_interval:int):
        self.index = index
        self.data_bytes = data_bytes
        self.ack_received:bool=False
        self.receive_timeout:int=TimeUtils.utc_time+receive_timeout_interval
    def __repr__(self):
        return f'[Partition: {self.index},{self.data_bytes}]'

class PartitionManager:
    def __init__(self, max_data_size=1024, old_data_clean_interval_sec=3.0):
        """
        ctor
        :param max_data_size: max size of each partitioned data part
        :param old_data_clean_interval_sec: when does a partitioned data part considered old and should be removed
        """
        self.old_data_clean_interval_sec = old_data_clean_interval_sec
        self.max_data_size = max_data_size

    def get_data_parts(self, data_bytes: bytes) -> List[Partition]:
        ret = []
        for i, j in enumerate(range(0, len(data_bytes), self.max_data_size)):
            partition = Partition(i, data_bytes[j:j + self.max_data_size])

            ret.append(partition)
        return ret

if __name__ == '__main__':
    pm = PartitionManager(6, 300)
    parts = pm.get_data_parts(b'01234567890123456789')
    print(parts)

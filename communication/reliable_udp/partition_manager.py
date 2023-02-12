from communication.reliable_udp.partition import Partition

class PartitionManager:
    def __init__(self, max_partition_size: int, resend_count: int):
        self.max_partition_size = max_partition_size
        self.resend_count = resend_count

    def create_partitions(self, data_bytes: bytes, message_id: int, target_ip: str, target_port: int) -> \
            list[Partition] | None:
        if not data_bytes:
            return None
        partitions: list[Partition] = []
        parts_data_bytes = [data_bytes[i:i + self.max_partition_size] for i in
                            range(0, len(data_bytes), self.max_partition_size)]

        for part_number, part_data_bytes in enumerate(parts_data_bytes):
            partition = Partition(message_id, part_number, len(parts_data_bytes), part_data_bytes, target_ip,
                                  target_port, 0.0, self.resend_count)
            partitions.append(partition)
        return partitions

if __name__ == '__main__':
    data = b'012345678912'
    for max_size, n_parts in zip(range(1, len(data) + 1), (12, 6, 4, 3, 3, 2, 2, 2, 2, 2, 2, 1)):
        pm = PartitionManager(max_size)
        partitions_a = pm.create_partitions(data, 111, "ip", 1)
        print(max_size, len(partitions_a) if partitions_a else None, partitions_a)
        n_parts_calc = len(partitions_a) if partitions_a else 0
        assert n_parts_calc == n_parts

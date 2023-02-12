from dataclasses import dataclass

@dataclass
class ReliableCommunicatorConfig:
    local_ip: str = ''
    local_port: int = -1
    receive_buffer_size: int = 64 * 1024
    max_partition_size: int = 63 * 1024  # value must be less than 65507

if __name__ == '__main__':
    c = ReliableCommunicatorConfig()
    print(c)

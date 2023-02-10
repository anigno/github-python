from dataclasses import dataclass

@dataclass
class ReliableCommunicatorConfig:
    local_ip: str = ''
    local_port: int = -1
    receive_buffer_size = 64 * 1024,
    max_partition_size = 63 * 1024  # value must be less than 65507

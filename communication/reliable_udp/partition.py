from dataclasses import dataclass

@dataclass
class Partition:
    message_id: int
    part_number: int
    total_parts: int
    part_data_bytes: bytes
    target_ip: str
    target_port: int
    sent_time: float
    resend_counter: int

if __name__ == '__main__':
    p = Partition(1, 2, 3, b'4', '5', 6, 0, 3)

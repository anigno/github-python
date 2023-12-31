from typing import Tuple

class DataReceivedEventArgs:
    def __init__(self, received_data_bytes: bytes, sender_endpoint_tuple: Tuple[str, int]):
        self.received_data_bytes = received_data_bytes
        self.sender_endpoint_tuple = sender_endpoint_tuple

    def __str__(self):
        return f'DataReceivedEventArgs:({self.received_data_bytes} {self.sender_endpoint_tuple})'

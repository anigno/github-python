from typing import Tuple

class MessageData:
    def __init__(self):
        self.message_type: int = 0
        self.data_bytes: bytes = b''
        self.sender_endpoint: Tuple[str, int] = ('', 0)

    def __str__(self):
        return f'MessageData(type={self.message_type} length={len(self.data_bytes)} sender={self.sender_endpoint})'

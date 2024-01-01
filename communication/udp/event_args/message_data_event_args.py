from typing import Tuple, Optional

from communication.udp.message_base import MessageBase

class MessageDataEventArgs:
    """received message data args"""
    def __init__(self):
        self.message_type: int = 0
        self.message: Optional[MessageBase] = None
        self.sender_endpoint: Tuple[str, int] = ('', 0)

    def __str__(self):
        return f'MessageData(type={self.message_type} sender={self.sender_endpoint})'

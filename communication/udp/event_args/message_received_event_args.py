from typing import Tuple, Optional

from communication.udp.udp_message_base import UdpMessageBase

class MessageReceivedEventArgs:
    """received message data args"""

    def __init__(self):
        self.message_type: int = 0
        self.message: Optional[UdpMessageBase] = None
        self.sender_endpoint: Tuple[str, int] = ('', 0)

    def __str__(self):
        return f'MessageData(type={self.message_type} sender={self.sender_endpoint})'

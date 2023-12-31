from typing import Optional, Tuple

class CrcErrorEventArgs:
    def __init__(self, sender_endpoint_tuple: Optional[Tuple[str, int]]):
        self.sender_endpoint_tuple: Optional[Tuple[str, int]] = sender_endpoint_tuple

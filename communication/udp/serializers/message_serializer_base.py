from abc import ABC, abstractmethod

from communication.udp.udp_message_base import UdpMessageBase

class MessageSerializerBase(ABC):
    @abstractmethod
    def to_buffer(self, message: UdpMessageBase) -> bytes:
        pass

    @abstractmethod
    def from_buffer(self, message_type: int, buffer: bytes) -> UdpMessageBase:
        pass

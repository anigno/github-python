from abc import ABC, abstractmethod

from communication.udp.message_base import MessageBase

class MessageSerializerBase(ABC):
    @abstractmethod
    def to_buffer(self, message: MessageBase) -> bytes:
        pass

    @abstractmethod
    def from_buffer(self, message_type: int, buffer: bytes) -> MessageBase:
        pass

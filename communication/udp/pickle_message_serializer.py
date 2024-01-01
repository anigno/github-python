import pickle
from abc import ABC, abstractmethod

from communication.udp.message_base import MessageBase

class MessageSerializerBase(ABC):
    @abstractmethod
    def to_buffer(self, message: MessageBase) -> bytes:
        pass

    @abstractmethod
    def from_buffer(self, message_type: int, buffer: bytes) -> MessageBase:
        pass

class PickleMessageSerializer(MessageSerializerBase):
    def to_buffer(self, message: MessageBase) -> bytes:
        return pickle.dumps(message)

    def from_buffer(self, message_type: int, buffer: bytes) -> MessageBase:
        return pickle.loads(buffer)

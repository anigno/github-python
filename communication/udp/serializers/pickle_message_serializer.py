import pickle

from communication.udp.message_base import MessageBase
from communication.udp.serializers.message_serializer_base import MessageSerializerBase

class PickleMessageSerializer(MessageSerializerBase):
    def to_buffer(self, message: MessageBase) -> bytes:
        return pickle.dumps(message)

    def from_buffer(self, message_type: int, buffer: bytes) -> MessageBase:
        return pickle.loads(buffer)

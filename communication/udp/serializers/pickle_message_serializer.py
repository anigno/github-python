import pickle
from communication.udp.udp_message_base import UdpMessageBase
from communication.udp.serializers.message_serializer_base import MessageSerializerBase

class PickleMessageSerializer(MessageSerializerBase):
    def to_buffer(self, message: UdpMessageBase) -> bytes:
        return pickle.dumps(message)

    def from_buffer(self, message_type: int, buffer: bytes) -> UdpMessageBase:
        return pickle.loads(buffer)

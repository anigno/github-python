import pickle
from abc import ABC

class MessageBase(ABC):
    """base class for messages that uses the pickle serialization"""
    MESSAGE_TYPE = 0

    def to_buffer(self) -> bytes:
        bytes_array = pickle.dumps(self)
        return bytes_array

    @staticmethod
    def from_buffer(bytes_array: bytes) -> object:
        return pickle.loads(bytes_array)

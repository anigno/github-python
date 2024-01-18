import pickle
import time
from abc import ABC
from enum import Enum
from threading import RLock

from common.printable_params import PrintableParams

class MessageTypeEnum(Enum):
    BASE = 100
    STATUS_UPDATE = 101
    CAPABILITIES_UPDATE = 102
    FLY_TO_DESTINATION = 103

class MessageBase(ABC):
    """base class for messages, uses pickle serialization"""
    MESSAGE_TYPE = MessageTypeEnum.BASE
    _message_id_counter = 1000
    _locker = RLock()

    def __init__(self):
        self.send_time = -1
        with MessageBase._locker:
            self.message_id = MessageBase._message_id_counter
            MessageBase._message_id_counter += 1

    def to_buffer(self) -> bytes:
        return pickle.dumps(self)

    def from_buffer(self, buffer: bytes):
        self.__dict__ = pickle.loads(buffer).__dict__

    def __str__(self):
        return f'[{type(self)}: {self.message_id} {self.send_time}]\n'
if __name__ == '__main__':
    class Message1(MessageBase):
        MESSAGE_TYPE = 2222

        def __init__(self):
            super().__init__()
            self.name = 'abc'
            self.data = [1, 2, 3]


    Message1()
    Message1()
    m = Message1()
    m.send_time = time.time()
    PrintableParams.print(m, True)

    b1 = m.to_buffer()
    m2 = Message1()
    m2.from_buffer(b1)
    PrintableParams.print(m2, True)


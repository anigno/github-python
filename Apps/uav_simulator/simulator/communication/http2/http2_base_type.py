from abc import ABC
from threading import RLock

from common.printable_params import PrintableParams

class Http2BaseType(ABC):
    """base class for messages, adds unique message_id field"""
    _message_id_counter = 1000
    _locker = RLock()

    def __init__(self):
        with Http2BaseType._locker:
            self.message_id = Http2BaseType._message_id_counter
            Http2BaseType._message_id_counter += 1

if __name__ == '__main__':
    class Message1(Http2BaseType):
        def __init__(self):
            super().__init__()
            self.name = 'abc'
            self.data = [1, 2, 3]

    Message1()
    Message1()
    Message1()
    PrintableParams.print(Message1(), True)

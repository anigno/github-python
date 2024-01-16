from abc import ABC
from threading import RLock

class UdpMessageBase(ABC):
    """base class for all messages used by message communicator"""
    MESSAGE_TYPE = 100
    _unique_id_counter = 1000
    _unique_id_locker = RLock()

    def __init__(self):
        with UdpMessageBase._unique_id_locker:
            self.message_id = UdpMessageBase._unique_id_counter
            UdpMessageBase._unique_id_counter += 1
        self.sent_time: int = 0

if __name__ == '__main__':
    from threading import Thread
    import time

    class SomeMessage(UdpMessageBase):
        def __init__(self):
            super().__init__()
            self.data = 'abc'

    s = set()

    def func():
        for _ in range(30):
            m = SomeMessage()
            s.add(m.message_id)
            print(f'{m.message_id} {len(s)}')

    Thread(target=func).start()
    Thread(target=func).start()
    Thread(target=func).start()
    Thread(target=func).start()

    time.sleep(1)
    input('enter to exit')

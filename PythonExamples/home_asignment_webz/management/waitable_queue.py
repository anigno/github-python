import datetime
import time
from queue import Queue
from threading import RLock, Thread

from PythonExamples.home_asignment_webz.logging.logger import Logger

class WaitableQueue:
    """queue implementation of put and get, where the get is limited to time interval"""

    def __init__(self, delay: int, max_size=1000):
        self.delay = delay
        self._queue = Queue(max_size)
        self.locker = RLock()
        self.last_get_time = datetime.datetime.min

    def put(self, item):
        if not self._queue.full():
            self._queue.put_nowait(item)

    def get(self):
        with self.locker:
            current_time = datetime.datetime.now()
            remain_delay = current_time - self.last_get_time
            if remain_delay.seconds < self.delay:
                time.sleep(self.delay - remain_delay.seconds)
            self.last_get_time = datetime.datetime.now()
            return self._queue.get()

if __name__ == '__main__':
    wq = WaitableQueue(2)
    for a in range(5):
        Logger.log(f'put {a}')
        wq.put(a)

    def get_value(args):
        for _ in range(5):
            v = wq.get()
            Logger.log(f'{args} get {v}')

    Thread(target=get_value,args=[1]).start()
    Thread(target=get_value,args=[2]).start()

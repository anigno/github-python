"""
Periodic run of registered handlers
"""
import datetime
import math
import threading
import time
from typing import Dict, Any


class AScheduler:
    def __init__(self, base_interval=0.1):
        self.base_interval = base_interval
        self.scheduledHandlersDict = {}
        self.timedHandlersDict = {}
        self.minInterval = 0

    def _build_timing_table(self):
        self.minInterval = min(self.scheduledHandlersDict.keys())
        self.timedHandlersDict = {}
        for key in self.scheduledHandlersDict.keys():
            self.timedHandlersDict[int(key / self.base_interval)] = self.scheduledHandlersDict[key]

    def register_handler(self, interval: float, handler):
        self.scheduledHandlersDict[interval] = handler
        self._build_timing_table()

    def timer_thread_start(self):
        counter = 0
        consumed_interval = 0
        while (True):
            time.sleep(self.base_interval - consumed_interval)
            counter += 1
            start = time.clock()
            for key in self.timedHandlersDict.keys():
                if counter % key == 0:
                    self.timedHandlersDict[key]()
            end = time.clock()
            consumed_interval += end - start

    def start(self):
        thread = threading.Thread(target=self.timer_thread_start)
        thread.start()
        thread.join()


if __name__ == '__main__':
    def some_handler_A():
        print(datetime.datetime.now().time(), 'A')


    def some_handler_B():
        print(datetime.datetime.now().time(), 'B')


    def some_handler_C():
        print(datetime.datetime.now().time(), 'C')


    timer = AScheduler(base_interval=.5)
    timer.register_handler(.5, some_handler_A)
    timer.register_handler(1.5, some_handler_B)
    timer.register_handler(2, some_handler_C)

    timer.start()

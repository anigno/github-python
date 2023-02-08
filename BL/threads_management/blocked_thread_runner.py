import threading
import time
from typing import Callable

from BL.threads_management.interval_thread_runner import IntervalThreadRunner

class BlockedThreadRunner(IntervalThreadRunner):
    """thread runner that can be blocked by BlockingThreadRunner"""
    def __init__(self, thread_name: str, activity_method: Callable, interval: float, locker: threading.Event):
        """
        @param thread_name:
        @param activity_method:
        @param interval: wake interval
        @param locker: Event to be locked on, same event must be given to the BlockingThreadRunner
        """
        super().__init__(thread_name, activity_method, interval)
        self.locker = locker

    def run(self):
        while self.is_continue:
            t0 = time.time()
            self.locker.wait()
            self.activity_method()
            self.sleep_delta(self.thread_name, t0, self.interval)

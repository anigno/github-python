import threading
import time
from typing import Callable

from BL.threads_management.interval_thread_runner import IntervalThreadRunner

class BlockingThreadRunner(IntervalThreadRunner):
    """used for important activity, will block any BlockedThreadRunner from starting new iteration when
    this activity is working"""

    def __init__(self, thread_name: str, activity_method: Callable, interval: float, locker: threading.Event):
        """
        @param thread_name:
        @param activity_method:
        @param interval: wake interval
        @param locker: the Event used to block, same event must be given to BlockedThreadRunner's
        """
        super().__init__(thread_name, activity_method, interval)
        self.interval = interval
        self.locker = locker

    def run(self):
        while self.is_continue:
            self.locker.clear()
            t0 = time.time()
            self.activity_method()
            self.locker.set()
            self.sleep_delta(self.thread_name, t0, self.interval)

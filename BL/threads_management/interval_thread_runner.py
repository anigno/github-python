import time
from typing import Callable

from BL.threads_management.thread_runner_base import ThreadRunnerBase

class IntervalThreadRunner(ThreadRunnerBase):
    """Thread will try and run every interval time"""

    def __init__(self, thread_name: str, activity_method: Callable, interval: float):
        """
        @param thread_name:
        @param activity_method:
        @param interval: wake interval
        """
        super().__init__(thread_name, activity_method)
        self.interval = interval

    def run(self):
        while self.is_continue:
            t0 = time.time()
            self.activity_method()
            self.sleep_delta(self.thread_name, t0, self.interval)

    @staticmethod
    def sleep_delta(thread_name: str, t0: float, interval: float):
        """
        Sleep remaining time between requested interval and time passed from given t0
        @param t0: time.time() of starting measurement
        @param interval: total time
        @param thread_name:
        """
        t1 = time.time()
        dt = t1 - t0
        sleep_time = interval - dt
        if sleep_time < 0:
            print(f'[thread_manager] Timeout in: {thread_name} {sleep_time}')
            sleep_time = 0
        time.sleep(sleep_time)

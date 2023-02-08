import threading
import time
from threading import Thread

from BL.threads_management.thread_runner_base import ThreadRunnerBase
from BL.threads_management.blocking_thread_runner import BlockingThreadRunner
from BL.threads_management.blocked_thread_runner import BlockedThreadRunner
from BL.threads_management.interval_thread_runner import IntervalThreadRunner
from common.simple_logger import log

class ThreadManager:
    """manage thread runners"""

    def __init__(self):
        self.threads = []
        self._threadCounter = {}

    def add_thread(self, thread_runner: ThreadRunnerBase) -> Thread:
        """
        @param thread_runner:
        @return: the newly created thread, usually used for join
        """
        thread = Thread(target=thread_runner.run, name=thread_runner.thread_name, args=[])
        self.threads.append(thread)
        thread.start()
        return thread

if __name__ == '__main__':
    manager = ThreadManager()

    def activity_a():
        log('a')
        time.sleep(0.1)

    def activity_b():
        log('bbb')
        time.sleep(0.3)

    def activity_c():
        log('cccccc')
        time.sleep(0.5)

    def activity_d():
        log('important activity')
        time.sleep(0.5)

    # manager.add_thread(SimpleThreadRunner('ta', activity_a))
    manager.add_thread(IntervalThreadRunner('tb', activity_b, 1))
    manager.add_thread(IntervalThreadRunner('tc', activity_c, 2))
    locker = threading.Event()
    manager.add_thread(BlockedThreadRunner('ta', activity_a, 1, locker))
    manager.add_thread(BlockingThreadRunner('tc', activity_d, 1, locker))

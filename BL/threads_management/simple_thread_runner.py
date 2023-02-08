from typing import Callable

from BL.threads_management.thread_runner_base import ThreadRunnerBase

class SimpleThreadRunner(ThreadRunnerBase):
    """Simple thread that runs when possible and managed by OS"""
    def __init__(self, thread_name: str, activity_method: Callable):
        super().__init__(thread_name, activity_method)

    def run(self):
        while self.is_continue:
            self.activity_method()

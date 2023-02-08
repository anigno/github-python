from abc import ABC
from typing import Callable

class ThreadRunnerBase(ABC):
    """base class for thread runners"""

    def __init__(self, thread_name: str, activity_method: Callable):
        self.is_continue = True
        self.thread_name = thread_name
        self.activity_method = activity_method

    def run(self):
        pass

    def stop(self):
        self.is_continue = False

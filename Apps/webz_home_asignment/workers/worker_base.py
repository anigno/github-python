from abc import ABC, abstractmethod
from queue import Queue
from threading import Thread

class WorkerBase(ABC):

    def __init__(self, unique_name: str, queue: Queue, worker_delay: float):
        self.worker_delay = worker_delay
        self.unique_name = unique_name
        self.is_running = True
        self.queue = queue
        self.worker_thread = Thread(target=self.target_method, name=unique_name, daemon=False)

    def start(self):
        self.worker_thread.start()

    def stop(self):
        self.is_running = False

    @abstractmethod
    def target_method(self):
        """thread target method"""
        pass

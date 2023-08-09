from abc import ABC, abstractmethod
from threading import Thread

from Apps.webz_home_asignment.data_access.data_access_base import DataAccessBase
from Apps.webz_home_asignment.management.waitable_queue import WaitableQueue

class WorkerBase(ABC):
    """base class for a worker, with target method run in a WorkManager's managed threads"""
    def __init__(self, unique_name: str, queue: WaitableQueue, data_access: DataAccessBase):
        self.data_access = data_access
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

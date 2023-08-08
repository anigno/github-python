import queue
import time
from queue import Queue
from typing import Type

from Apps.webz_home_asignment.workers.crawler_queue_item import CrawlerQueueItem
from Apps.webz_home_asignment.workers.worker_base import WorkerBase

class WorkManager:
    QUEUE_MAX_SIZE = 1_000_000;

    def __init__(self, work_manager_config_dict: dict,
                 worker_thread_type: Type[WorkerBase]):
        self.worker_thread_type = worker_thread_type
        self._worker_name_prefix = work_manager_config_dict["worker_name_prefix"]
        self._number_of_workers = work_manager_config_dict["number_of_workers"]
        self._worker_delay = work_manager_config_dict["worker_delay"]
        self._workers: list[WorkerBase] = []
        self.working_queue = Queue(WorkManager.QUEUE_MAX_SIZE)
        self._init_workers()

    def _init_workers(self):
        for i in range(self._number_of_workers):
            worker_unique_name = self._worker_name_prefix + str(i)
            worker_instance = self.worker_thread_type(worker_unique_name, self.working_queue, self._worker_delay)
            self._workers.append(worker_instance)

    def start(self, url: str):
        queue_item = CrawlerQueueItem(url=url)
        self.working_queue.put(queue_item)
        for worker_thread in self._workers:
            worker_thread.start()

    def stop(self):
        for worker in self._workers:
            worker.stop()

if __name__ == '__main__':
    from Apps.webz_home_asignment.workers.worker_crawler import WorkerCrawler

    wm_config = {"worker_name_prefix": "worker_", "number_of_workers": 2}
    wm = WorkManager(work_manager_config_dict=wm_config, worker_thread_type=WorkerCrawler)
    wm.start()
    time.sleep(1.5)
    wm.stop()

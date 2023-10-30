from typing import Type, Optional

from PythonExamples.home_asignments.home_asignment_webz.data_access.data_access_json import DataAccessJson
from PythonExamples.home_asignments.home_asignment_webz.management.waitable_queue import WaitableQueue
from PythonExamples.home_asignments.home_asignment_webz.workers.crawler_queue_item import CrawlerQueueItem
from PythonExamples.home_asignments.home_asignment_webz.workers.worker_base import WorkerBase

class WorkManager:
    """creates and manage working threads implemented as workers"""
    QUEUE_MAX_SIZE = 1_000_000

    def __init__(self, work_manager_config_dict: dict,
                 worker_thread_type: Type[WorkerBase]):
        # read configuration
        self._worker_name_prefix = work_manager_config_dict["worker_name_prefix"]
        self._number_of_workers = work_manager_config_dict["number_of_workers"]
        self._worker_delay = work_manager_config_dict["worker_delay"]
        # create components
        self.worker_thread_type = worker_thread_type
        self._workers: list[WorkerBase] = []
        self.working_queue = WaitableQueue(delay=self._worker_delay, max_size=WorkManager.QUEUE_MAX_SIZE)
        self.data_access = DataAccessJson(work_manager_config_dict["products_folder"])
        self.login_worker: Optional[WorkerBase] = None
        # additional init
        self._init_workers()

    def _init_workers(self):
        """create workers instances"""
        for i in range(self._number_of_workers):
            worker_unique_name = self._worker_name_prefix + str(i)
            worker_instance = self.worker_thread_type(worker_unique_name, self.working_queue, self.data_access)
            self._workers.append(worker_instance)
            self.login_worker = worker_instance

    def login(self, login_url):
        self.login_worker.login(login_url)
        # TODO: check if session failed

    def start(self, url: str, login_url: str = ''):
        """login and start workers threads"""
        if login_url:
            self.login(login_url)
        queue_item = CrawlerQueueItem(url=url, data='main')
        self.working_queue.put(queue_item)
        for worker in self._workers:
            worker.start()

    def stop(self):
        """"""
        for worker in self._workers:
            worker.stop()

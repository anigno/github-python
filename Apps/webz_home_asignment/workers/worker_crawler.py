import random

from Apps.webz_home_asignment.data_access.data_access_base import DataAccessBase
from Apps.webz_home_asignment.data_access.data_access_json import DataAccessJson
from Apps.webz_home_asignment.logging.logger import Logger
from Apps.webz_home_asignment.management.waitable_queue import WaitableQueue
from Apps.webz_home_asignment.workers.crawler_queue_item import CrawlerQueueItem
from Apps.webz_home_asignment.workers.worker_base import WorkerBase

class WorkerCrawler(WorkerBase):
    """specialized worker for a requested site (TurkHacks)"""

    def __init__(self, unique_name: str, queue: WaitableQueue, data_access: DataAccessBase):
        super().__init__(unique_name, queue, data_access)

    def target_method(self):
        while self.is_running:
            queue_item = self.queue.get()
            self.crawl(queue_item)

    def crawl(self, queue_item: CrawlerQueueItem):
        """extraction method for requested site"""
        Logger.log(f'{self.unique_name}->crawling url: {queue_item.url}')
        Logger.log("generate dammy data")
        self.queue.put(CrawlerQueueItem("https://www.turkhacks.com/forum/sosyal-medya-hacking.184/"))
        data = {"page_link": "https://www.turkhacks.com/forum/sosyal-medya-hacking.184/",
                "title": "Turk Hacks",
                "published_time": "1/1/2023",
                "content": "whatever"}
        self.data_access.save_data(self.unique_name, data)

"""
Turk Hacks
subject list
general posts

subject
posts

"""

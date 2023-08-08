import random
import time
from queue import Queue

from Apps.webz_home_asignment.logging.logger import Logger
from Apps.webz_home_asignment.workers.crawler_queue_item import CrawlerQueueItem
from Apps.webz_home_asignment.workers.worker_base import WorkerBase

class WorkerCrawler(WorkerBase):
    def __init__(self, unique_name: str, queue: Queue[CrawlerQueueItem], worker_delay: float):
        super().__init__(unique_name, queue, worker_delay)

    def target_method(self):
        while self.is_running:
            # time.sleep(random.randint(1000, 2000) / 1000)
            queue_item = self.queue.get()
            self.crawl(queue_item)

    def crawl(self, queue_item: CrawlerQueueItem):
        Logger.log(f'{self.unique_name}->crawling url: {queue_item.url}')



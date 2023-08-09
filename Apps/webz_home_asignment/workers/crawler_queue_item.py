class CrawlerQueueItem:
    """crawler data in queue"""

    def __init__(self, url: str, data=''):
        self.url = url
        self.data = data

import time
from logging_initiator import LoggingInitiator
import logging

class SomeClass:
    def __init__(self):
        LoggingInitiator.init_logging()

        # self.logger = logging.getLogger('main_logger')
        self.logger = logging.getLogger('stream_only_logger')

    def run(self):
        while True:
            self.logger.debug("hello")
            time.sleep(0.3)

if __name__ == '__main__':
    c = SomeClass()
    c.run()

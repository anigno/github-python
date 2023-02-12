import logging
import random
import time

from logging_provider.logging_initiator import LoggingInitiator

class TestApp:
    def __init__(self):
        LoggingInitiator()
        logger = logging.getLogger(LoggingInitiator.MAIN_LOGGER)
        for i in range(400):
            level = random.randint(0, 5) * 10
            long_string = '123456789_' * 1000
            logger.log(level=level, msg=f'{i} {long_string}')
            time.sleep(0.1)

if __name__ == '__main__':
    app = TestApp()

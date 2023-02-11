import json
import logging.config
import logging.handlers
import os
import random
import time

class LoggingInitiator:
    @staticmethod
    def init_logging(logging_config_file: str = 'logging_config.json'):
        abs_path=os.path.abspath(logging_config_file)
        if not os.path.exists(abs_path):
            raise FileNotFoundError(abs_path)
        logging_config_file = logging_config_file
        logging.config.dictConfig(json.load(open(abs_path, 'r')))
        logging.addLevelName(logging.WARNING, "WARN")
        logging.addLevelName(logging.CRITICAL, "FATAL")

if __name__ == '__main__':
    logger = logging.getLogger('main_logger')
    text = '123456789_' * 1000
    rnd = random.Random()
    for a in range(1000000):
        b = rnd.randint(0, 5 + 1)
        if b == 0:
            logger.debug(f'{a}: {text}')
        elif b == 1:
            logger.info(f'{a}: {text}')
        elif b == 2:
            logger.warning(f'{a}: {text}')
        elif b == 3:
            logger.error(f'{a}: {text}')
        elif b == 4:
            logger.fatal(f'{a}: {text}')
        elif b == 5:
            logger.exception(f'{a}: {text}')
        time.sleep(.1)

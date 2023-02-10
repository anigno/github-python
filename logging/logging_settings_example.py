import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("$%(asctime)s|%(threadName)s|%(levelname)s|%(module)s,%(funcName)s|%(message)s")

file_handler = logging.FileHandler(filename="sample.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

if __name__ == '__main__':
    def func01():
        logger.debug("hello")
        logger.debug("world")
    func01()

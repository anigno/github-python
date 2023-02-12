import logging
import sys

from logging_provider.reverse_rotating_file_handler import ReverseRotatingFileHandler

class LoggingInitiator:
    STREAM_LOGGER = "stream_only_logger"
    MAIN_LOGGER = "main_logger"

    def __init__(self, log_files_path="d:/dev/logs/log"):
        logging.addLevelName(logging.WARNING, "WARN")
        logging.addLevelName(logging.CRITICAL, "FATAL")
        """
        Using json config file:
            logging.config.dictConfig(json.load(open(logging_config_file, 'r')))
            logging.addLevelName(logging.WARNING, "WARN")
            logging.addLevelName(logging.CRITICAL, "FATAL")
            logger = logging.getLogger('main_logger')
        """
        log_viewer_formatter = logging.Formatter(
            "$%(asctime)s|%(threadName)s|%(levelname)s|%(module)s,%(funcName)s|%(message)s")

        main_file_handler = ReverseRotatingFileHandler(prefix="log.txt", path=log_files_path, mode="a",
                                                       max_bytes=2_097_152,
                                                       backup_count=1000, delay=False)
        main_file_handler.formatter = log_viewer_formatter
        main_file_handler.setLevel(logging.DEBUG)

        main_stream_handler = logging.StreamHandler(stream=sys.stdout)
        main_stream_handler.formatter = log_viewer_formatter
        main_stream_handler.setLevel(logging.DEBUG)

        main_logger = logging.getLogger(LoggingInitiator.MAIN_LOGGER)
        main_logger.setLevel(logging.DEBUG)
        main_logger.addHandler(main_file_handler)
        main_logger.addHandler(main_stream_handler)

        stream_only_logger = logging.getLogger(LoggingInitiator.STREAM_LOGGER)
        stream_only_logger.setLevel(logging.DEBUG)
        stream_only_logger.addHandler(main_stream_handler)

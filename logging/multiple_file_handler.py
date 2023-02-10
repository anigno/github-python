import logging
from logging import LogRecord
from pathlib import Path
from typing import Dict

from core.logger.reverse_rotating_file_handler import ReverseRotatingFileHandler


class MultipleFileHandler(logging.Handler):
    def __init__(self, path: str, prefix: str, mode: str, max_bytes, backup_count):
        super().__init__()
        self._base_dir = Path(path)
        self._prefix = prefix
        self._mode = mode
        self._max_bytes = max_bytes
        self._backup_count = backup_count
        self._components: Dict[str, ReverseRotatingFileHandler] = {}

    def emit(self, record: LogRecord) -> None:
        component_id = record.name.partition('.')[-1]
        component_id = component_id.lower()
        if component_id not in self._components:
            component_dir = self._base_dir / component_id
            component_dir.mkdir(parents=True, exist_ok=True)
            self._components[component_id] = ReverseRotatingFileHandler(self._prefix, component_dir, self._mode, self._max_bytes, self._backup_count)
            self._components[component_id].formatter = self.formatter
            self._components[component_id].level = self.level
            self._components[component_id].filters = self.filters
            self._components[component_id].name = self.name
        self._components[component_id].handle(record)


def client_log(component_id: str):
    return logging.getLogger(f'client.{component_id}')


if __name__ == '__main__':
    client_logger = logging.getLogger('client')
    client_logger.setLevel(logging.DEBUG)
    client_logger.addHandler(logging.StreamHandler())
    client_logger.addHandler(MultipleFileHandler('d:/_/TEST', "log.txt", 'a', 30, 30))

    client_log('comp1').info('test1!')
    client_log('comp2').info('test2!')
    client_log('comp1').info('test11!')
    client_log('comp2').info('test22!')

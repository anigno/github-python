import logging.handlers
import time
from pathlib import Path


class ReverseRotatingFileHandler(logging.handlers.RotatingFileHandler):
    """Do a reverse rollover , according to log4net requirements."""

    def __init__(self, prefix, path, mode, max_bytes, backup_count, encoding='utf-8', delay=False):
        filename = f"{prefix}_{time.strftime('%d-%m-%Y')}_{time.strftime('%H-%M-%S')}"
        attempts_left = 2
        if path is not None:
            dir_path = Path(path)
            while not dir_path.exists() and attempts_left > 0:
                try:
                    attempts_left -= 1
                    dir_path.mkdir(parents=True, exist_ok=True)
                except ValueError as e:
                    print(f'Failed to create the directory {dir_path}: {e}. Trying again.')
            file_path = dir_path / filename
        else:
            file_path = Path(filename)
        self.last_file_num = 1
        super().__init__(str(file_path) + '.1', mode, max_bytes, backup_count, encoding, delay)
        self.baseFilename = str(file_path)

    def doRollover(self):  # OVERRIDE
        """Do a reverse rollover , according to log4net requirements."""
        if self.stream:
            self.stream.close()
            self.stream = None
        if self.backupCount > 0:
            self.last_file_num += 1
            if self.last_file_num > self.backupCount:
                self.last_file_num = 1
        if not self.delay:
            self.stream = open(self.baseFilename + '.' + str(self.last_file_num), 'w', encoding=self.encoding)

import datetime
from threading import RLock

class Logger:
    """simple implementation on console log"""

    _locker = RLock()

    @staticmethod
    def log(message: str):
        with Logger._locker:
            print(f'{datetime.datetime.utcnow()}: {message}')

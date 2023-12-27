import datetime
from threading import RLock

_logLocker = RLock()

def log(message: str):
    with _logLocker:
        print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} {message}")

if __name__ == '__main__':
    log('hello')

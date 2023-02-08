from datetime import datetime

def log(message: str):
    print(f"{datetime.strftime(datetime.now(), '%H:%M:%S.%f')} {message}")

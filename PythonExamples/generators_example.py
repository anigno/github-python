import time
from threading import RLock, Thread

locker = RLock()

def numbers_generator():
    for a in range(1, 10):
        yield a

gen = numbers_generator()

def thread_start():
    while True:
        with locker:
            try:
                v = next(gen)
            except StopIteration:
                break
        print(v)
        time.sleep(1)

Thread(target=thread_start, daemon=True).start()
Thread(target=thread_start, daemon=True).start()
Thread(target=thread_start, daemon=True).start()

input('enter to exit')

import threading
import time
from datetime import datetime


def controlledThreadFunction(setWaitEvent: threading.Event):
    while (True):
        isTimedOut = not setWaitEvent.wait(1.3)
        print(threading.current_thread().name, datetime.now().time(), 'isTimedOut:', isTimedOut)
        setWaitEvent.clear()


def controllingThreadFunction(setWaitEvent: threading.Event):
    while (True):
        time.sleep(2)
        setWaitEvent.set()
        print(datetime.now().time(), 'set')


if __name__ == '__main__':
    setWaitEvent = threading.Event()
    t1 = threading.Thread(target=controlledThreadFunction, name='Controlled_1', args=(setWaitEvent,))
    t3 = threading.Thread(target=controlledThreadFunction, name='Controlled_2', args=(setWaitEvent,))
    t2 = threading.Thread(target=controllingThreadFunction, name='Controller', args=(setWaitEvent,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()

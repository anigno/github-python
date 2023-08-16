import threading
from signal import signal
from threading import RLock, Condition

def locker():
    locker_rlock = RLock()
    with locker_rlock:
        pass
    locker_condition = Condition()
    locker_condition.acquire()
    locker_condition.release()
    locker_condition.notify()
    locker_condition.notify_all()
    locker_condition.wait(555)
    locker_condition.wait_for(lambda x: x < 5, 300)

    event = threading.Event()
    event.set()
    event.wait(100)
    event.clear()






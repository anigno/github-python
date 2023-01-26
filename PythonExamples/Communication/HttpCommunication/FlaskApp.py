import datetime
import math
import multiprocessing
import random
import threading
import time
from multiprocessing import Process
from FlaskServer import process_func  # not an error, stupid pycharm can't find the files


def start_process(child_queue):
    p = Process(target=process_func, args=(parent_queue, child_queue,))
    p.start()


def doSomething(child_queue, receivedData):
    print(datetime.datetime.now().time(), 'doSomething', 'started', receivedData)
    a = random.randint(100, 1000)
    time.sleep(a)
    print(datetime.datetime.now().time(), 'doSomething', 'ended', receivedData)
    child_queue.put_nowait(receivedData)


if __name__ == '__main__':
    parent_queue = multiprocessing.Queue(10)
    child_queue = multiprocessing.Queue(10)
    start_process(child_queue)
    while (True):
        if parent_queue.empty():
            time.sleep(0.001)
        else:
            keyAndRequest = parent_queue.get_nowait()
            threading.Thread(target=doSomething, args=[child_queue, keyAndRequest]).start()

"""
greenlets scheduling
"""
import asyncio
import threading

from gevent import greenlet
from gevent.queue import Queue

_periodic_run_loop = asyncio.get_event_loop()


def schedulerFunction():
    gMain = greenlet.greenlet(run=test1)
    pass


thread = threading.Thread(target=schedulerFunction)


def start() -> threading.Thread:
    thread.start()
    return thread


def add_task(task, priority):

    pass

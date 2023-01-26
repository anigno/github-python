"""
Decorator for running periodic tasks, using asyncio main loop thread to run registered functions,
tasks must not block!
"""
import asyncio
import threading
import time

from Decorators.UtilDecorators import time_measure_between_calls

_periodic_run_loop = asyncio.get_event_loop()
_periodic_tasks = []


def periodic_run(interval: int):
    def internal(func):
        def wrapperFunc(*args, **kwargs):
            t0 = time.clock()
            ret = func(*args, **kwargs)
            t1 = time.clock()
            nextDelay = interval - (t1 - t0)
            if nextDelay < 0:
                print('timeout',interval,nextDelay)
            _periodic_run_loop.call_later(delay=nextDelay, callback=wrapperFunc)
            return ret

        _periodic_tasks.append(wrapperFunc)
        return wrapperFunc

    return internal


def _start():
    _periodic_run_loop.run_forever()


def start() -> threading.Thread:
    for t in _periodic_tasks:
        _periodic_run_loop.call_soon(t)
    thread = threading.Thread(target=_start)
    thread.start()
    return thread


def stop():
    _periodic_run_loop.stop()


if __name__ == '__main__':
    import math


    # @time_measure_function_decorator
    def do_work(number):
        for a in range(0, number):
            b = math.sqrt(a)


    @periodic_run(1)
    @time_measure_between_calls
    def worker_A1():
        do_work(100000)


    @periodic_run(1)
    @time_measure_between_calls
    def worker_A2():
        do_work(100000)


    @periodic_run(2)
    @time_measure_between_calls
    def worker_B():
        do_work(2000000)


    @periodic_run(3)
    @time_measure_between_calls
    def worker_C():
        do_work(100000)


    @periodic_run(4)
    @time_measure_between_calls
    def worker_D():
        do_work(100000)

    print('started')
    start()
    time.sleep(12)
    stop()

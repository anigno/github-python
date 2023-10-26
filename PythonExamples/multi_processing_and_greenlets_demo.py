import math
import multiprocessing
import threading
import time

from gevent import greenlet

MAX_VAL = 10000000


def calc_thread_start(startEndTuple: tuple):
    start, end = startEndTuple
    name = threading.current_thread().getName()
    print(name, 'Starting', start, end)
    # time.sleep(0.5)
    for a in range(start, end):
        b = math.sqrt(a)
    print(name, 'Finished', end - start, 'sqrt numbers')


if __name__ == '__main__':
    print('****** One thread')
    thread = threading.Thread(target=calc_thread_start, args=((0, MAX_VAL),))
    t0 = time.clock()
    thread.start()
    thread.join()
    t1 = time.clock()
    print('Finished', t1 - t0, 'sec')
    print()

    print('****** Multiple thread')
    thread1 = threading.Thread(target=calc_thread_start, args=((MAX_VAL * 0 // 3, MAX_VAL * 1 // 3),))
    thread2 = threading.Thread(target=calc_thread_start, args=((MAX_VAL * 1 // 3, MAX_VAL * 2 // 3),))
    thread3 = threading.Thread(target=calc_thread_start, args=((MAX_VAL * 2 // 3, MAX_VAL * 3 // 3),))
    t0 = time.clock()
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    t1 = time.clock()
    print('Finished', t1 - t0, 'sec')
    print()

    print('****** gevent.greenlets')


    def test1():
        calc_thread_start((MAX_VAL * 0 // 3, MAX_VAL * 1 // 3))
        gr2.switch()


    def test2():
        calc_thread_start((MAX_VAL * 1 // 3, MAX_VAL * 2 // 3))
        gr3.switch()


    def test3():
        calc_thread_start((MAX_VAL * 2 // 3, MAX_VAL * 3 // 3))


    gr1 = greenlet.greenlet(run=test1)
    gr2 = greenlet.greenlet(run=test2)
    gr3 = greenlet.greenlet(run=test3)
    t0 = time.clock()
    gr1.switch()
    t1 = time.clock()
    print('Finished', t1 - t0, 'sec')
    print()

    print('****** process pool')
    process_pool = multiprocessing.Pool(3)
    print()

    t0 = time.clock()
    process_pool.map(func=calc_thread_start, iterable=[
        (MAX_VAL * 0 // 3, MAX_VAL * 1 // 3),
        (MAX_VAL * 1 // 3, MAX_VAL * 2 // 3),
        (MAX_VAL * 2 // 3, MAX_VAL * 3 // 3)])
    t1 = time.clock()
    print('Finished', t1 - t0, 'sec')
    print()

import math
import time

import gevent
import threading

MAX_NUMBERS = 1000000
MAX_DEV = 1000


def calc_roots(numbers):
    for a in numbers:
        b = math.sqrt(a)


groups = [range(a, a + MAX_DEV-1) for a in range(0, MAX_NUMBERS, MAX_DEV)]

print('greenlets')
start = time.clock()
jobs = [gevent.spawn(calc_roots, group) for group in groups]
gevent.joinall(jobs, timeout=10)
stop = time.clock()
print(stop - start)

print('threads')
start = time.clock()
for group in groups:
    thread = threading.Thread(target=calc_roots, args=(group,))
    thread.start()
    thread.join()
stop = time.clock()
print(stop - start)

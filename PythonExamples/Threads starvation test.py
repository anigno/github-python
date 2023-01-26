import math
import threading
import time

from Decorators.typeVerifier import typeVerifier

totalTime=[0,0,0]
breakAll=False

@typeVerifier
def listSum(aList:list)->float:
    total=0
    for item in aList:
        total+=item
    return total

def ThreadStartMethod(threadNumber: str):
    global totalTime,breakAll
    for a in range(0,300):
        if breakAll:
            break
        print(threadNumber,a)
        # measure start
        startClock=time.clock()
        for b in range(0,100000):
            c=math.sqrt(b)
        endClock=time.clock()
        # measure end
        totalTime[threadNumber]+= endClock - startClock
        # time.sleep(0.001)
    breakAll=True
    print(f'Time in thread: {threadNumber} is: {totalTime[threadNumber]} all: {listSum(totalTime)} Clock {time.clock()}')

threading.Thread(target=ThreadStartMethod, args=[0]).start()
threading.Thread(target=ThreadStartMethod, args=[1]).start()
threading.Thread(target=ThreadStartMethod, args=[2]).start()

# import queue
# import random
#
# q = queue.PriorityQueue()
# for i in range(0, 10):
#     r = random.randint(10, 20)
#     q.put((r, str(r*r)))
#
# while (True):
#     print(q.qsize(), q.get())

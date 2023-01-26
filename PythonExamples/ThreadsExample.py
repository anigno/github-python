import time
from threading import Thread, Lock, RLock
from gevent import greenlet
myLock = RLock()
commonValueA = 0
commonValueB = 0


def AddA(v):
    global commonValueA, commonValueB
    while True:
        myLock.acquire()    #once
        commonValueA += v   #twice
        myLock.acquire()
        myLock.release()    #once
        myLock.release()    #Twice
        commonValueB += v
        print('AddA', commonValueA,commonValueB)
        # time.sleep(0.1)


def AddB(v):
    global commonValueA, commonValueB
    while True:
        with myLock:
            commonValueA += v
        commonValueB += v
        print('AddB', commonValueA,commonValueB)
        # time.sleep(0.1)


if __name__ == '__main__':
    Thread(target=AddA, args=(1,)).start()
    Thread(target=AddB, args=(1,)).start()

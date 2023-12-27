import threading
import time
from queue import Queue
from threading import Thread

from Logging.ConsoleLogger import ConsoleLogger
import math

DEFAULT_WORK_COUNT = 10000
TAL_WORK_COUNT = 50000
logger = ConsoleLogger()
queueDixH = Queue()
queueDixL = Queue()
queueClientsH = Queue()
queueClientsL = Queue()
locker = threading.Event()
threadCounter = {}


def sleepDelta(t0, interval):
    t1 = time.clock()
    dt = t1 - t0
    sleepTime = interval - dt
    if sleepTime < 0:
        logger.logDebug(f'Timeout in: {threading.currentThread().name} {sleepTime}')
        sleepTime = 0
    time.sleep(sleepTime)


def addThreadCount():
    threadCounter[threading.currentThread().name] = threadCounter.get(threading.currentThread().name, 0) + 1


def threadFunc_dixH(receiveFunc):
    while True:
        locker.wait()
        addThreadCount()
        receiveFunc()
        time.sleep(0)


def threadFunc_clientsH(receiveFunc):
    while True:
        locker.wait()
        addThreadCount()
        receiveFunc()
        time.sleep(0)


def threadFunc_dixL(receiveFunc):
    while True:
        locker.wait()
        addThreadCount()
        receiveFunc()
        time.sleep(0)


def threadFunc_clientsL(receiveFunc):
    while True:
        locker.wait()
        addThreadCount()
        receiveFunc()
        time.sleep(0)


def threadFunc_T(talFunc):
    while True:
        locker.clear()
        t0 = time.clock()
        addThreadCount()
        talFunc()
        locker.set()
        sleepDelta(t0, 0.167)

def threadFunc_R(reportsWaitableFunc, waitEvent: threading.Event, statusToConsoleFunc, clientsConnectivityFunc, warningSammaryFunc, procedureCancelinfCheckFunc):
    cnt = 0
    while True:
        t0 = time.clock()
        addThreadCount()
        reportsWaitableFunc(waitEvent)
        clientsConnectivityFunc()
        procedureCancelinfCheckFunc()
        cnt+=1
        if cnt >= 4:
            statusToConsoleFunc()
            warningSammaryFunc()
            cnt = 0
        sleepDelta(t0, 1.000)


def threadFunc_D(db_function):
    while True:
        t0 = time.clock()
        addThreadCount()
        db_function()
        sleepDelta(t0, 20.000)


def threadFunc_N(acks_function, safety_function, retransmit_function):
    while True:
        t0 = time.clock()
        addThreadCount()
        acks_function()
        safety_function()
        retransmit_function()
        sleepDelta(t0, 1.000)


if __name__ == '__main__':

    def messageProducerThreadFunc():
        cnt = 1000
        while True:
            queueDixH.put(f'dix message {cnt}')
            time.sleep(.020)
            cnt += 1
            queueDixL.put(f'dix message {cnt}')
            time.sleep(.020)
            cnt += 1
            queueClientsH.put(f'client message {cnt}')
            time.sleep(.020)
            cnt += 1
            queueClientsL.put(f'client message {cnt}')
            time.sleep(.020)
            cnt += 1


    # @time_measure_function_decorator
    def doSomething(workCnt):
        # logger.logDebug(threading.currentThread().name)
        for a in range(workCnt):
            math.sqrt(workCnt)


    def doSomethingConst():
        doSomething(DEFAULT_WORK_COUNT)


    def monitoringThreadFunc():
        delay = 5.000
        while True:
            time.sleep(delay)
            totalTime = time.clock()
            logger.logInfo(f'*************** total time: {totalTime}')
            for key in threadCounter.keys():
                logger.logInfo(f'********** {key} cnt={threadCounter[key]} iterTime={round(totalTime/threadCounter[key],3)}')
            logger.logInfo(f'********** {queueDixH.qsize()} {queueDixL.qsize()} {queueClientsH.qsize()} {queueClientsL.qsize()}')


    # @time_measure_function_decorator
    def talFunction():
        # logger.logDebug(f'tal start {time.clock()}')
        doSomething(TAL_WORK_COUNT)


    def dixH_receiveFunction():
        queueDixH.get()
        doSomething(DEFAULT_WORK_COUNT)


    def dixL_receiveFunction():
        queueDixL.get()
        doSomething(DEFAULT_WORK_COUNT)


    def clientsH_receiveFunction():
        queueClientsH.get()
        doSomething(DEFAULT_WORK_COUNT)


    def clientsL_receiveFunction():
        queueClientsL.get()
        doSomething(DEFAULT_WORK_COUNT)


    def reportsWaitable_function(waitEvent: threading.Event):
        for a in range(5):
            waitEvent.wait()
            doSomething(DEFAULT_WORK_COUNT * 10)


    def db_function():
        doSomething(DEFAULT_WORK_COUNT)


    def acks_function():
        doSomething(DEFAULT_WORK_COUNT)


    def safety_function():
        doSomething(DEFAULT_WORK_COUNT)


    def retransmit_function():
        doSomething(DEFAULT_WORK_COUNT)


    # fill queues with start test data
    for a in range(10000):
        queueDixH.put(f'message {a}')
    for a in range(10000):
        queueDixL.put(f'message {a}')
    for a in range(10000):
        queueClientsH.put(f'message {a}')
    for a in range(10000):
        queueClientsL.put(f'message {a}')

    # Thread(target=messageProducerThreadFunc).start()

    Thread(target=monitoringThreadFunc).start()

    Thread(target=threadFunc_T, name='Tal', args=[talFunction]).start()
    Thread(target=threadFunc_dixH, name='dixH', args=[dixH_receiveFunction]).start()
    Thread(target=threadFunc_dixH, name='dixL', args=[dixL_receiveFunction]).start()
    Thread(target=threadFunc_clientsH(), name='clientsH', args=[clientsH_receiveFunction]).start()
    Thread(target=threadFunc_clientsL(), name='clientsL', args=[clientsL_receiveFunction]).start()

    Thread(target=threadFunc_R, name='R', args=[reportsWaitable_function, locker, doSomethingConst, doSomethingConst, doSomethingConst, doSomethingConst]).start()
    Thread(target=threadFunc_D, name='D', args=[db_function]).start()
    Thread(target=threadFunc_N, name='N', args=[acks_function, safety_function, retransmit_function]).start()

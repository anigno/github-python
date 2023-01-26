import logging
import logging.handlers
import queue
import sys
import threading
import time


class SimpleLogger(object):

    timedQueue=queue.Queue(-1)

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        logHandler = logging.StreamHandler(sys.stderr)
        # logHandler = logging.FileHandler('d:\\temp\\logTest.txt')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logHandler.setFormatter(formatter)

        # Non blocking log writes
        loggingQueue = queue.Queue(-1)
        queueHandler = logging.handlers.QueueHandler(loggingQueue)
        listener = logging.handlers.QueueListener(loggingQueue, logHandler)
        listener.start()
        self.logger.addHandler(queueHandler)

        # Blocking log writes
        # self.logger.addHandler(logHandler)
        self.TimerMethod()



    def debugTimed(self, msg, *args, **kwargs):
        self.timedQueue.put((msg,args,*kwargs))


    def TimerMethod(self):
        print('Queue size: {0}'.format(self.timedQueue.qsize()))
        while self.timedQueue.qsize()>0:
            m=self.timedQueue.get()
            logger.logger.debug(m)
        threading.Timer(1, self.TimerMethod).start()




logger = SimpleLogger()

def ThreadStartMethod(name, delay):
    for i in range(0, 10000):
        # logger.logger.debug("%s %i", name, i)
        logger.debugTimed("%s %i", name, i)
        time.sleep(delay)


threading.Thread(target=ThreadStartMethod, args=['A', 0.001]).start()
threading.Thread(target=ThreadStartMethod, args=['B', 0.002]).start()
threading.Thread(target=ThreadStartMethod, args=['C', 0.003]).start()

print("Started")

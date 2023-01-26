import random
import threading
import time
from multiprocessing import Pipe, Process

from Logging.ConsoleLogger import ConsoleLogger


def processStartWithPipes(pipes):
    logger = ConsoleLogger()
    # use pipe[1] here for sending and receiving (not crossed)
    for a in range(10):
        pipes[1].send(a)
        logger.logDebug(f'sent {a}')


def receiverTask(*args):
    receivedData=args[0]
    logger.logInfo(f'receiverTask started:{receivedData}')
    time.sleep(random.randint(100,1000)/1000)
    logger.logInfo(f'receiverTask ended:{receivedData}')



if __name__ == '__main__':
    logger = ConsoleLogger()
    q=random.seed(10)
    logger.logDebug(q)
    pipes = Pipe(duplex=True)
    p1 = Process(target=processStartWithPipes, args=(pipes,))
    p1.start()
    while True:
        receivedData = pipes[0].recv()
        # logger.logDebug(f'__main__ received:{receivedData}')
        threading.Thread(target=receiverTask, args=(receivedData,)).start()

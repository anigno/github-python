import time
from multiprocessing import Pipe, Process, Queue


def processStartWithQueues(parentQueue: Queue, childQueue: Queue):
    parentQueue.put('a')
    print('processStartWithQueues received:', childQueue.get())


def processStartWithPipes(pipes):
    # use pipe[1] here for sending and receiving (not crossed)
    pipes[1].send('c')
    print('processStartWithPipes received:', pipes[1].recv())


if __name__ == '__main__':
    parentQueue = Queue(10)
    childQueue = Queue(10)
    p1 = Process(target=processStartWithQueues, args=(parentQueue, childQueue))
    p1.start()
    print('__main__ received:', parentQueue.get())
    childQueue.put('b')

    pipes = Pipe(duplex=True)
    p1 = Process(target=processStartWithPipes, args=(pipes,))
    p1.start()
    # use pipe[0] here for sending and receiving (not crossed)
    print('__main__ received', pipes[0].recv())
    pipes[0].send('d')

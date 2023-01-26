import threading
import time
from multiprocessing import Pipe, Process
from threading import Thread


def barrierPassFunc():
    print('barrierPassFunc')

def threadFunc(barrier:threading.Barrier):
    print('threadFunc waiting')
    barrier.wait(5)
    print('threadFunc passed barrier')

if __name__ == '__main__':
    print('Barrier will wait for 3 threads')
    barrier = threading.Barrier(parties=3, action=barrierPassFunc, timeout=10)
    print('Starting two of three threads')
    threading.Thread(target=threadFunc, name='A', args=(barrier,)).start()
    threading.Thread(target=threadFunc, name='B', args=(barrier,)).start()
    time.sleep(2)
    print('starting third thread')
    threading.Thread(target=threadFunc, name='C', args=(barrier,)).start()

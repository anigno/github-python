from multiprocessing import Process, Queue, Pipe

import time


def queuePutNumbers(w):
    for a in range(0,10):
        w.put(['number',a])
        print('put',a)
        time.sleep(.6)

def queueGet():
    q = Queue()
    p = Process(target=queuePutNumbers, args=(q,))
    p.start()
    time.sleep(2)
    while True:
        print('get',q.get())
        time.sleep(.5)



def pipeSending(pipe):
    for a in range(1,6):
        pipe.send(a)
        print('sent',a)
        time.sleep(0.1 * a)

def pipeReceive():
    (parent_conn, child_conn) = Pipe()
    Process(target=pipeSending, args=(child_conn,)).start()
    while True:
        t=parent_conn.poll(timeout=0.3)
        a=parent_conn.recv()
        print('received',a,t)

if __name__ == '__main__':
    # queueGet()
    pipeReceive()

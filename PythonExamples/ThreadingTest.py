import threading

import time


def ThreadStartMethod(name, delay):
    i=0
    while True:
        print(name, i)
        time.sleep(delay)
        i+=1


threading.Thread(target=ThreadStartMethod, args=['A', 1.2]).start()
threading.Thread(target=ThreadStartMethod, args=['B', 1.4]).start()
threading.Thread(target=ThreadStartMethod, args=['C', 1.5]).start()

for a in range(0, 10000):
    print('main', a)
    time.sleep(1)


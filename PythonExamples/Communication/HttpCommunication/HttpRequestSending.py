import datetime
import time
from threading import Thread

import requests


def ThreadStartMethod(args):
    clientKey = args[0]
    maxRequests = 10
    totalTime = 0
    for i in range(0, maxRequests):
        sentData = f'[messageId:{clientKey}{i} {datetime.datetime.now().time()}]'
        start = time.clock()
        response = requests.post(url='http://10.108.102.29:8080/doSomething/', data=sentData)
        stop = time.clock()
        totalTime += (stop - start)
        print(datetime.datetime.now().time(), 'sent:', sentData, 'received:', response.content,stop-start)
    print(clientKey, 'total time:', totalTime)


if __name__ == '__main__':
    Thread(target=ThreadStartMethod, args=['A']).start()
    # Thread(target=ThreadStartMethod, args=['B']).start()
    # Thread(target=ThreadStartMethod, args=['C']).start()
    # Thread(target=ThreadStartMethod, args=['D']).start()
    # Thread(target=ThreadStartMethod, args=['E']).start()
    # Thread(target=ThreadStartMethod, args=['F']).start()
    # Thread(target=ThreadStartMethod, args=['G']).start()
    # Thread(target=ThreadStartMethod, args=['H']).start()

    # r = requests.post(url='http://10.108.102.29:8080/something', data='Hello', json="{'k1':'v1'}")
    # print(time.clock(),r)
    # r = requests.put(url='http://10.108.102.29:8080/something', data='Hello', json="{'k1':'v1'}")
    # print(time.clock(),r)
    # time.sleep(1)
    # r = requests.delete(url='http://10.108.102.29:8080/something', data='Hello', json="{'k1':'v1'}")
    # print(time.clock(),r)
    # time.sleep(1)
    # r = requests.get(url='http://10.108.102.29:8080/something', data='Hello', json="{'k1':'v1'}")
    # print(time.clock(),r)

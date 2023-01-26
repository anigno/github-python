import time
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

def thread_func(name: str):
    b = 0
    for a in range(5):
        print(f'{name} : {b}')
        b += 1
        time.sleep(0.1)
    return name + ' done'

def main():
    # executor = ThreadPoolExecutor(max_workers=2)
    executor = ProcessPoolExecutor(max_workers=2)
    # run threads from pool
    a1 = executor.submit(thread_func, 'A')
    a2 = executor.submit(thread_func, 'B')
    a3 = executor.submit(thread_func, 'C')
    # print return value when ready (futures)
    print(a1.result())
    print(a2.result())
    print(a3.result())

    print('---------------------------')
    iter1 = executor.map(thread_func, ['D', 'E'])
    # force iteration run in threads
    list1 = list(iter1)
    # print return values
    print(list1)
    executor.shutdown()

if __name__ == '__main__':
    main()

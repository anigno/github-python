import time
from concurrent.futures import ThreadPoolExecutor

def thread_func(name: str):
    b = 0
    print(f'{name} started')
    for a in range(5):
        b += 1
        time.sleep(0.1)
    print(f'{name} end')

    return name + ' result'

def main():
    executor = ThreadPoolExecutor(max_workers=2)
    executers = []

    # run threads from pool
    for a in 'ABCDE':
        executers.append(executor.submit(thread_func, a))

    for future in executers:
        print(future.result())
    # print return value when ready (futures)

    print('---------------------------')
    executor.shutdown()

if __name__ == '__main__':
    main()

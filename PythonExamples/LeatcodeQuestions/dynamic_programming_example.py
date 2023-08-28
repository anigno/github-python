import time

"""
dynamic programming solution
1. draw the spanning recursive tree that solves the problem
2. find re-occurring nodes and their key
3. store results of each node after returning from recurse call
4. before calling a recurse call, check if key already exist and return its value
"""

def calc_fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calc_fib(n - 2) + calc_fib(n - 1)

def calc_fib_dynamic(n: int, storage_dict: dict):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # check if already calculated n-1 to retrieve from storage
    if (n - 1) not in storage_dict:
        fib1 = calc_fib_dynamic(n - 1, storage_dict)
        storage_dict[n - 1] = fib1
    fib1 = storage_dict[n - 1]
    # check if already calculated n-2 to retrieve from storage
    if (n - 2) not in storage_dict:
        fib2 = calc_fib_dynamic(n - 2, storage_dict)
        storage_dict[n - 2] = fib2
    fib2 = storage_dict[n - 2]
    return fib1 + fib2

if __name__ == '__main__':
    start = time.time()
    for i in range(35):
        print(f'{i}: {calc_fib(i)}')
    print(time.time() - start)

    storage = {}
    start = time.time()
    for i in range(350):
        print(f'{i}: {calc_fib_dynamic(i, storage)}')
    print(time.time() - start)

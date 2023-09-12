import random
from typing import List

def iterate_unique(nums: List[int]):
    unique_dict = {}
    for a in nums:
        if a not in unique_dict:
            unique_dict[a] = None
            yield a
        else:
            continue

if __name__ == '__main__':
    rand_list = [random.randint(0, 10) for _ in range(10)]

    for a in rand_list:
        print(f'{a} ', end='')
    print()

    for a in iterate_unique(rand_list):
        print(f'{a} ', end='')
    print()

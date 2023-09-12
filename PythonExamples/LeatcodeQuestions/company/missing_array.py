from typing import List

def find_missing_number(arry: List[int]) -> int:
    sum1 = sum(arry)
    sum2 = sum(range(len(arry) + 2))
    return sum2 - sum1

def find_missing_two_numbers(arry: List[int]) -> list:
    d = {}
    ret = []
    for a in arry:
        d[a] = None
    for a in range(1, len(arry) + 3):
        if a not in d:
            ret.append(a)
    return ret

if __name__ == '__main__':
    arry1 = [1, 3, 4, 5]
    print(find_missing_number(arry1))
    arry1 = [1, 3, 4, 6, 7]
    print(find_missing_two_numbers(arry1))

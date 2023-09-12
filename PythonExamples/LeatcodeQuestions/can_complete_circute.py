from typing import List

def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """find where to start if adding gas value  , and subtracting cost , will get you to where
    you have started"""
    # build gain list
    length = len(gas)
    gain = []
    for a in range(length):
        gain.append(gas[a] - cost[a])
    # print(gain)
    # look for start
    start = 0
    end = 0
    steps = 0
    gain_count = 0
    order_count = 0
    while steps < length:
        order_count += 1
        gain_count += gain[end]
        if gain_count < 0:
            if start != end:
                if end<start:
                    return -1
                start = end
            else:
                start = (start + 1)
                if start >= length:
                    return -1
            if start == 0:
                return -1
            steps = 0
            end = start
            gain_count = 0
        else:
            end = (end + 1) % length
            steps += 1
    print(f'order count: {order_count} length: {length}')
    return start

if __name__ == '__main__':
    print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(can_complete_circuit([2, 3, 4], [3, 4, 3]))
    print(can_complete_circuit([5,1, 1, 2, 3, 4], [4,1, 4, 1, 5, 1]))
    print(can_complete_circuit(
        [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
         95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
         25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
         53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66],
        [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
         55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
         83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
         13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]))

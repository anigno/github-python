from typing import List

def min_jumps(nums: List[int]) -> int:
    """return the minimum number of jumps"""
    a = len(nums) - 1
    jumps = [99999] * len(nums)
    jumps[a] = 0  # last cell is targeted
    while a >= 0:
        # take the min jumps of possible next steps
        c = a + nums[a] + 1
        for b in range(a + 1, c):
            if b >= len(nums):
                break
            jumps[a] = min(jumps[a], jumps[b] + 1)
        a -= 1
    return jumps[0]

# 232214
#
if __name__ == '__main__':
    print(min_jumps([2, 3, 2, 2, 1, 4]))
    print(min_jumps([2, 3, 1, 1, 4]))
    print(min_jumps([2, 3, 0, 1, 4]))
    print(min_jumps([2, 2, 0, 0, 4])) # no answer

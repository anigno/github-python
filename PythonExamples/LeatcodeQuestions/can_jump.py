from typing import List

def can_jump(nums: List[int]) -> bool:
    """each number represent the jump distance, find if able to reach to end to nums,
    e.g.
    3,3,0,0,4 - can jump 3 from [0] or left with 2 from [1], but [1] is 3, so can jump 3 from [1],
    check remaining jumps with old value compare to new jump value and take larger to continue"""
    if len(nums) < 2:
        return True
    a = 0
    max_jump = nums[0]
    while max_jump > 0:
        max_jump = max(max_jump - 1, nums[a])
        a += 1
        if a == len(nums):
            return True
    return False

if __name__ == '__main__':
    print(can_jump([3, 3, 0, 0, 4]))
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))
    print(can_jump([3, 0, 0, 0, 1, 4]))
    print(can_jump([3, 0, 0, 1, 4]))
    print(can_jump([0]))

# 23114
# 0 2>_
# 1 3>(2-1)
# 2 (3-1)>1
# 3 (3-2)>1
# 4 finished succeeded

# 32104
# 0 3>_
# 1 (3-1)>2
# 2 (3-2)>1
# 3 (3-3)>0
# finished failed

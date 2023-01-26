from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for a in range(0, len(nums)):
            d[target - nums[a]] = a
        for a in range(0, len(nums)):
            if nums[a] in d:
                if a != d[nums[a]]:
                    return [a, d[nums[a]]]

    # 2 5 5 9 11 =10
    # 2,3,4 = 5

print(Solution().twoSum([3, 2, 4], 6))

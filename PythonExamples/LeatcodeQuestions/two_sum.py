from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """find two indexes of numbers that sum target"""
        nums2 = nums.copy()
        nums.sort()
        a = 0
        b = len(nums) - 1
        while nums[a] + nums[b] != target:
            current_sum = nums[a] + nums[b]
            if current_sum < target:
                a += 1
            if current_sum > target:
                b -= 1
            if a == b:
                return [-1, -1]
        index1 = nums2.index(nums[a])
        nums2[index1] = -1
        index2 = nums2.index(nums[b])
        return [index1, index2]

if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]

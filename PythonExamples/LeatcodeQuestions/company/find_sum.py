from typing import List

class Solution:
    def find_sum_numbers(self, nums: List[int], target: int) -> tuple[int, int]:
        """find two numbers in nums that sum target O(nlog(n))"""
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left != right:
            t = nums[left] + nums[right]
            if t < target:
                left += 1
            elif t > target:
                right -= 1
            else:
                return nums[left], nums[right]

    def find_sum_indexes(self, nums: List[int], target: int) -> tuple[int, int]:
        """return indexes og found numbers O(n)"""
        pos_dict = {}
        # build dict by nums:[indexes]
        for i, num in enumerate(nums):
            if num not in pos_dict:
                pos_dict[num] = []
            pos_dict[num].append(i)
        # try to create pairs that sum target
        for k, v in pos_dict.items():
            remain = target - k
            i1 = v.pop()
            if remain in pos_dict and len(pos_dict[remain]):
                i2 = pos_dict[remain].pop()
                return i1, i2
        return -1, -1

# 312543 6
# build dict 3,0,5 1:1 2:2 5:3 4:4
# iterate dict keys, take first number and look for target-number in dict again

if __name__ == '__main__':
    s = Solution()
    print(s.find_sum_numbers([3, 1, 2, 5, 4, 3], 6))
    print(s.find_sum_numbers([1, 1, 1, 2, 3], 3))

    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 6))
    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 7))
    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 4))
    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 5))
    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 9))
    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 8))
    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 3))
    print(s.find_sum_indexes([3, 1, 2, 5, 4, 3], 1))

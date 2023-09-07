from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        k = 0
        while a < len(nums):
            if nums[a] == val:
                nums.remove(val)
                # del (nums[a])
                k+=1
                a-=1
            a+=1
        return k


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(s.removeElement(nums, val))
    print(nums)

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(s.removeElement(nums, val))
    print(nums)

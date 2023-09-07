from typing import List

# remove more than two duplicates in a sorted array
# [0, 1, 1, 1, 1, 2, 3, 3, 4] -> [0, 1, 1, 2, 3, 3, 4]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        b = 1
        k = 0
        c = 0
        if len(nums) <= 2:
            return len(nums)
        while b < len(nums):
            print(f'{nums} c={c}->', end='')
            if nums[a] != nums[b]:
                nums[c] = nums[a]
                c += 1
                k += 1
                a += 1
                b += 1
            elif nums[a] == nums[b]:
                while b < len(nums) and nums[a] == nums[b]:
                    b += 1
                nums[c] = nums[a]
                nums[c + 1] = nums[a]
                a = b
                b = a + 1
                k += 2
                c += 2
            if b == len(nums):
                nums[c] = nums[a]
                k += 1
            print(f'{nums} c={c}')
        return k

if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 1, 1, 1, 2, 3, 3, 4]
    # nums = [1, 1, 1, 2, 2, 3]
    # nums = [1]
    k = s.removeDuplicates(nums)
    print(k, nums[:k])
    # [0, 1, 1, 2, 3, 3, 4]

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        merge two non-descending lists
        Do not return anything, modify nums1 in-place instead.
        """
        a = 0
        b = 0
        while a < m + n and b < n:
            if nums1[a] > nums2[b]:
                nums1.insert(a, nums2[b])
                nums1.pop()
                b += 1
            a += 1
        c = b
        while b < n:
            nums1.pop()
            b += 1
        while c < n:
            nums1.append(nums2[c])
            c += 1

if __name__ == '__main__':
    s = Solution()
    tests = [[[1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3],
             [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
             [[4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3],
             [[4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5]]
    for test in tests:
        s.merge(test[0], test[1], test[2], test[3])
        print(test[0])

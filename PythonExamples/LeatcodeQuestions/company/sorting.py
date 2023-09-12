from typing import List
import heapq

def sort_o2(nums: List[int]):
    for a in range(len(nums)):
        for b in range(len(nums)):
            if nums[a] < nums[b]:
                nums[a], nums[b] = nums[b], nums[a]

def heap_sort(nums: list):
    heap_storage = []
    for n in nums:
        heapq.heappush(heap_storage, n)
    nums.clear()
    for _ in range(len(heap_storage)):
        nums.append(heapq.heappop(heap_storage))

def merge_sort(nums: list):
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    # merge sorted left and right
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    # check for leftovers
    while i < len(left):
        nums[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        nums[k] = right[j]
        k += 1
        j += 1

def binary_search(sorted_list: list, num: int):
    mid = len(sorted_list) // 2
    if sorted_list[mid] == num: return mid
    if num < sorted_list[mid]:
        return binary_search(sorted_list[:mid], num)
    else:
        return mid+binary_search(sorted_list[mid:], num)

if __name__ == '__main__':
    nums = [3, 6, 5, 4, 5, 6, 8, 9, 8, 7, 2, 1, 3, 4, 5, 6]
    sort_o2(nums)
    print(nums)
    nums = [3, 6, 5, 4, 5, 6, 8, 9, 8, 7, 2, 1, 3, 4, 5, 6]
    heap_sort(nums)
    print(nums)
    nums = [3, 6, 5, 4, 5, 6, 8, 9, 8, 7, 2, 1, 3, 4, 5, 6]
    merge_sort(nums)
    print(nums)
    print(binary_search(nums, 7))

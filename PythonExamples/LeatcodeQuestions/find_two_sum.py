def find_two_sum(nums: list[int], target) -> list[int]:
    nums.sort()
    a = 0
    b = len(nums) - 1
    while b < len(nums):
        if nums[a] + nums[b] < target:
            a += 1
        elif nums[a] + nums[b] > target:
            b -= 1
        elif nums[a] + nums[b] == target:
            return [nums[a], nums[b]]

if __name__ == '__main__':
    print(find_two_sum([3, 6, 1, 1, 4, 5, 6, 7, 2, 4, 7, 6, 2, 4, 5, 6], 6))
    print(find_two_sum([3, 6, 1, 1, 4, 5, 6, 7, 2, 4, 7, 6, 2, 4, 5, 6], 6))
    print(find_two_sum([3, 6, 1, 1, 4, 5, 6, 7, 2, 4, 7, 6, 2, 4, 5, 6], 7))

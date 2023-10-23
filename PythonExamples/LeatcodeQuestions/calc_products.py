def calc_products(nums: list[int]) -> list[int]:
    """calc products of each num in nums, without its value, without using '/' """
    # build lists of products starting from left to right and right to left
    length = len(nums)
    products_right = [1] * length
    products_left = [1] * length
    pr = 1
    pl = 1
    for a in range(length):
        pl = pl * nums[a]
        pr = pr * nums[length - a - 1]
        products_left[a] = pl
        products_right[length - a - 1] = pr
    # calculate return
    nums[0] = products_right[1]
    nums[length - 1] = products_left[length - 2]

    for a in range(1, length - 1):
        nums[a] = products_left[a - 1] * products_right[a + 1]
    return nums

if __name__ == '__main__':
    print(calc_products([1, 2, 3, 4]))
    print(calc_products([-1, 1, 0, -3, 3]))

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """buy and sell many times"""
        profit_sum = 0
        left = 0
        right = 1
        cp = 0
        while right < len(prices):
            cp = prices[right] - prices[left]
            if cp < 0:
                left = right
                right = left + 1
            elif right < len(prices) - 1 and prices[right + 1] < prices[right]:
                cp = prices[right] - prices[left]
                profit_sum += cp
                print(f' {cp} {profit_sum}')
                left = right
                right = left + 1
                cp = 0
            else:
                right += 1
        profit_sum += max(cp, 0)
        return profit_sum

# 241
# 24 2
# 13 2
# 14 3
# 15 4
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 6, 3, 6, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([1]))
    print(s.maxProfit([0, 1]))
    print(s.maxProfit([2, 4, 1]))

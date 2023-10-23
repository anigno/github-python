from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """find best profit buy and sell once, check each buy index as long as there is a profit.
        if no profit , move to index after the no profit found index"""
        maxp = 0
        left_buy = 0
        right_sell = 1
        while right_sell < len(prices):
            p = prices[right_sell] - prices[left_buy]
            maxp = max(p, maxp)
            # if found smaller buy price, lets check if it has a sell prise for better profit
            if prices[right_sell] < prices[left_buy]:
                left_buy = right_sell
            right_sell += 1
        return maxp

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 0, 6]))
    print(s.maxProfit([2, 5, 3, 1, 3]))

# 715306
# 71 0 :start with 7
# 15 4 :1 is better buy then 7 profit is 4
# 06 :0 is better buy, check if has a sell then makes better profit then previous 4
# 6 is the best profit

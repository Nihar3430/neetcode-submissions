class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit_max = 0

        while right < len(prices):
            if prices[right] >= prices[left]:
                profit_max = max(profit_max, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1

        return profit_max

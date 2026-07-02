class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        l = 0
        r = 0

        temp_profit = prices[r] - prices[l]

        max_profit = max(temp_profit, max_profit)

        while r < len(prices) - 1:
            if prices[r] < prices[l]:
                l = r
            else:
                r += 1

            temp_profit = prices[r] - prices[l]

            max_profit = max(temp_profit, max_profit)

            
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, max_profit = 0, 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            profit = prices[R] - prices[L]
            max_profit = max(max_profit, profit)
        return max_profit

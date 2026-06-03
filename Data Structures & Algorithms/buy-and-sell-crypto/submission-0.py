class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        min_idx = None
        max_val = float('-inf')


        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
                min_idx = i
        
        max_val = max(prices[min_idx:])
        
        return max_val - min_val
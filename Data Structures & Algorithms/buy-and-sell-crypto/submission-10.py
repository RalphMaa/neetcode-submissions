class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_val)
            if prices[i]<min_val:
                min_val = prices[i]
        
        return max_profit
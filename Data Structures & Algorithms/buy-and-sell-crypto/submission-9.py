class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        max_profit = 0
        for left in range(len(prices)):
            
            for right in range(left+1, len(prices), +1):
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)

        return max_profit
            
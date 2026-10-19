class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        t = 0
        if amount == 0:
            return 0

        min_num = {}
        

        # I am assuming there is at least 1 solution -> Need to find a way to treat that edge case when no solution is found

        def dfs(total, target): # Returns the min number of counts to get to target (aka amount)
            # Edge cases
            if total == target:
                return 0
            elif total > target:
                return math.inf
            elif total in min_num:
                return min_num[total]
            
            min_coins = math.inf

            for i in coins:
                min_coins = min(min_coins, 1+dfs(total+i, target))
            
            min_num[total] = min_coins
                
            
            return min_coins
        
        min_coins = dfs(0,amount)

        if min_coins == math.inf:
            return -1

        return min_coins





class Solution:
    def climbStairs(self, n: int) -> int:

        fib = [0]*n
        
        def dfs(curr) -> int:
            if curr>n:
                return 0
            

            if curr==n:
                return 1

            if fib[curr]>0:
                return fib[curr]




            
            fib[curr] = dfs(curr+1)+dfs(curr+2)

            return fib[curr]

        
        
        return dfs(0)

        
            

            


            





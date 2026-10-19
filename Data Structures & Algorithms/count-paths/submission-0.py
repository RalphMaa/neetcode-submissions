class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # DFS with cache
        cache = []

        for r in range(m):
            cache.append([0] * n)
        
        def dfs(r, c):
            # 1. base case: at the bottom-right corner → return ___
            # 2. base case: off the grid (r >= m or c >= n) → return ___
            # 3. memo hit → return cache[r][c]

            if r == m-1 and c == n-1:
                return 1
            elif r >= m or c >= n:
                return 0
            elif cache[r][c] > 0:
                return cache[r][c]
            
            # 4. answer = dfs(___, ___)  ___  dfs(___, ___)   # down, right, combined how?
            answer = dfs(r+1, c) + dfs(r, c+1) 

            # 5. store answer in cache, return it
            cache[r][c] = answer

            return answer
        
        return dfs(0, 0)

        

        




            

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        max_row, max_col = len(obstacleGrid), len(obstacleGrid[0])
        # DFS with cache -> 2D-Dynamic programming
        cache = []
        for i in range(max_row):
            cache.append([-1] * max_col)
        
        # print("Max_row: ", max_row)
        # print("Max_col: ", max_col)
        # print()
    
        
        def dfs(curr_row, curr_col):
            # Edge case 1: Arrived at a border or obstacle return 0

            # print("Curr_row: ", curr_row)
            # print("Curr_col: ", curr_col)
            if curr_row <0 or curr_row>=max_row or curr_col<0 or curr_col>=max_col or obstacleGrid[curr_row][curr_col] == 1:
                # print("Obstacle Reached")
                # print()
                return 0
            elif curr_row == max_row-1 and curr_col == max_col-1:
                # print("Objective Reached")
                # print()
                return 1
            elif cache[curr_row][curr_col] >= 0:
                # print("Cache Reached")
                # print()
                return cache[curr_row][curr_col]
            
            res = dfs(curr_row+1, curr_col) + dfs(curr_row, curr_col+1)

            cache[curr_row][curr_col] = res

            return res
        
        return dfs(0, 0)

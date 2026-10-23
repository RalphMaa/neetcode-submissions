class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited = []
        for row in range(ROWS):
            visited.append([False] * COLS)

        def dfs(row, col):
            
            if row<0 or row>=ROWS or col<0 or col>=COLS or grid[row][col]==0 or visited[row][col]==True:
                return 0
            curr_area = 1
            visited[row][col] = True
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                curr_area += dfs(new_row, new_col)

            
            return curr_area        

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and visited[row][col] == False:

                    # DFS
                    curr_area = dfs(row, col)
                    max_area = max(max_area, curr_area)
        
        return max_area

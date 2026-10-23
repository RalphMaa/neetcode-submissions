class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        max_area = 0

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited = []
        for row in range(ROWS):
            visited.append([False] * COLS)


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and visited[row][col] == False:

                    # BFS
                    queue = collections.deque([[row, col]])
                    visited[row][col] = True
                    curr_area = 0
                    
                    while queue:
                        curr_row, curr_col = queue.popleft()
                        
                        curr_area += 1

                        for dr, dc in directions:
                            new_row = curr_row + dr
                            new_col = curr_col+dc

                            # Check every direction if there is a valid move
                            if new_row>=0 and new_row<ROWS and new_col>=0 and new_col<COLS and grid[new_row][new_col]==1 and visited[new_row][new_col] == False:
                                queue.append([new_row, new_col])
                                visited[new_row][new_col] = True
                                
                    max_area = max(curr_area, max_area)
        
        return max_area



                    
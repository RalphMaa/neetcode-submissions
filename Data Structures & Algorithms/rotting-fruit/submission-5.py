class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        num_fresh_fruit = 0
        num_fresh_to_rotten = 0
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        visit = []
        for i in range(ROWS):
            visit.append([False] * COLS)
        
        min_minutes = 0


        queue = collections.deque([])
        num_visited_rotten_fruits = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    visit[row][col] = True
                    queue.append([row, col])
        
        num_visited_rotten_fruits = len(queue)
                
        new_rotten = False
        while queue:
            curr_row, curr_col = queue.popleft()
            num_visited_rotten_fruits -= 1
            
            for dr, dc in directions:
                if (curr_row+dr>=0 and curr_row+dr<ROWS) and (curr_col+dc>=0 and curr_col+dc<COLS) and (visit[curr_row+dr][curr_col+dc] == False ) and grid[curr_row+dr][curr_col+dc] == 1:
                    new_rotten = True
                    grid[curr_row+dr][curr_col+dc] = 2
                    visit[curr_row+dr][curr_col+dc] = True
                    queue.append([curr_row+dr, curr_col+dc])
            
            
            if new_rotten == True and num_visited_rotten_fruits == 0:
                min_minutes += 1
                num_visited_rotten_fruits = len(queue)
                new_rotten = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                        
        
        return min_minutes
        

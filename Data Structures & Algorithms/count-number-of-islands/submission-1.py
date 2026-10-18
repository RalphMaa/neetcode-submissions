class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) # Borders of Matrix
        visit = []
        for i in range(ROWS):
            visit.append([False]*COLS)
        
        num_islands = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0" or  visit[r][c] == True:
                    continue
                else:
                    # We are on an island -> Use BFS to find the visited nodes of the island
                    queue = collections.deque([[r, c]])
                    num_islands += 1
                    # FIFO -> .popleft()

                    while queue:
                        curr_pos = queue.popleft()
                        for dr, dc in directions:

                            
                            if curr_pos[0]+dr>=0 and curr_pos[0]+dr<ROWS and curr_pos[1]+dc>=0 and curr_pos[1]+dc<COLS and (visit[curr_pos[0]+dr][curr_pos[1]+dc] == False ) and grid[curr_pos[0]+dr][curr_pos[1]+dc]=="1":
                                # Perform BFS
                                visit[curr_pos[0]+dr][curr_pos[1]+dc] = True
                                valid_pos = [curr_pos[0]+dr, curr_pos[1]+dc]
                                queue.append(valid_pos)

 
        return num_islands
                    
                                





        




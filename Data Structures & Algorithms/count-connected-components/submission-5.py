class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        connected_graphs = 0
        visit = [0] * n
        for curr_node in range(n):
            if visit[curr_node] == 0:
                queue = collections.deque([curr_node])
                while queue:
                    node = queue.popleft()
                    visit[node] = 1
                    for i in range(len(edges)):
                        if edges[i][0] == node and visit[edges[i][1]] == 0:
                            queue.append(edges[i][1])
                        elif edges[i][1] == node and visit[edges[i][0]] == 0:
                            queue.append(edges[i][0])
                
                connected_graphs += 1
            
        return connected_graphs
                



            

            
        







        




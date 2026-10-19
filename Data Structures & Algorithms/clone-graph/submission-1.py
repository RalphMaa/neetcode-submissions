"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # Will use BFS
        queue = collections.deque([node]) # Start from the root node
        deep_copy = {node: Node(node.val)} # Keep track of the OLD and NEW COPY
        
        # Start the search
        while queue: # While it's not empty -> Visit the next node in the queue
            curr_node = queue.popleft()

            # Loop through the neighbors for the curr_node
            for neig in curr_node.neighbors:
                # Need to check if the neig is not in visited
                if neig not in deep_copy:
                    deep_copy[neig] = Node(neig.val) # Add neig to deep_copy
                    queue.append(neig) # Add neig to the queue
                deep_copy[curr_node].neighbors.append(deep_copy[neig])


        

        return deep_copy[node]
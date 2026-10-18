# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use BFS

        # Edge case: Empty root
        if not root:
            return []
        
        queue = deque([[root, 0]])
        res = []
        
        # Need to keep track of the depth so that we know where we need to add the values in which sub-list

        level = 0
        while queue:
            node, level = queue.popleft()
            if len(res)-1 < level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            if node.left:
                queue.append([node.left, level + 1])
                
            if node.right:
                queue.append([node.right, level + 1])
            
            
        return res

            

            
        

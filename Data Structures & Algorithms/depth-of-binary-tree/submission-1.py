# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        #Initialize stack for DFS
        stack = deque([(root, 1)])
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            left = node.left
            right = node.right
            if right:
                stack.append((right, depth+1))
            if left:
                stack.append((left, depth+1))
            
        
        return max_depth
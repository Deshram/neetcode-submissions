# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total_gn = 0
        max_val = -101
        
        def dfs(root, max_val):
            nonlocal total_gn

            if not root: return 
            
            if root.val >= max_val:
                total_gn+=1
                max_val = root.val

            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, max_val)

        return total_gn


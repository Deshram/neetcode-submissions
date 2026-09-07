# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root):
        if not root: return 0, True

        left_height, left_balanced = self.dfs(root.left)

        if not left_balanced: return left_height, False
        
        right_height, right_balanced = self.dfs(root.right)

        if not right_balanced: return right_height, False

        if abs(left_height - right_height) <= 1:
            res = True
        else:
            res = False

        return 1+max(left_height, right_height), res

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        max_height, res = self.dfs(root)

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countDepth(self, root, currDepth):
        if not root: return currDepth
        currDepth += 1

        leftDepth = self.countDepth(root.left, currDepth)
        currDepth = max(leftDepth, self.countDepth(root.right, currDepth))    

        return currDepth
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        currDepth = 0
        return self.countDepth(root, currDepth)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root, subroot):
        if not root and not subroot:
            return True

        if (not root and subroot) or (root and not subroot):
            return False

        if root.val == subroot.val:
            return (self.sameTree(root.left, subroot.left) and (self.sameTree(root.right, subroot.right)))

        return False
    
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)



       


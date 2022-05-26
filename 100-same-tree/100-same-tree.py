# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(root1,root2):
            if(root1==None and root2==None):
                return 1
            if(root1==None or root2==None):
                return 0
            left=same(root1.left,root2.left)
            right=same(root1.right,root2.right)
            return left and right and root1.val==root2.val
        return same(p,q)
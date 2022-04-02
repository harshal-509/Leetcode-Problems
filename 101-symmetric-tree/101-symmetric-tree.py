# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(root1,root2):
            if(root1==None and root2==None):
                return 1
            if((root1!=None and root2==None) or (root2!=None and root1==None)):
                return 0
            if(root1.val!=root2.val):
                return 0
            a=solve(root1.left,root2.right) and solve(root1.right,root2.left)
            return a
        return solve(root,root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root):
            if(root==None):
                return None
            if(root==p):
                return root
            if(root==q):
                return root
            x=solve(root.left)
            y=solve(root.right)
            if(x and not(y)):
                return x
            if(y and not(x)):
                return y
            if(x and y):
                return root
        return solve(root)
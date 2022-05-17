# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans=cloned
        def solve(root):
            if(root==None):
                return None
            if(root.val==target.val):
                return root
            a=solve(root.left)
            if(a):
                return a
            b=solve(root.right)
            if(b):
                return b
        return solve(ans)
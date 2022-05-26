# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root,s,c):
            if(root==None):
                return 0
            if(root.left==None and root.right==None):
                if(root.val+c==s):
                    return 1
            return solve(root.left,s,c+root.val) or solve(root.right,s,c+root.val)
        return solve(root,targetSum,0)
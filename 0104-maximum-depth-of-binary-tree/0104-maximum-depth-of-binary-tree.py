# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def hs(root):
            if(root==None):
                return 0
            return max(hs(root.left),hs(root.right))+1
        return hs(root)
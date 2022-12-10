# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
mod=int(1e9+7)
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.m=0
        def hs1(root):
            if(root==None):
                return 0
            return hs1(root.left)+hs1(root.right)+root.val
        def hs(root):
            if(root==None):
                return 0
            else:
                q=hs(root.left)+hs(root.right)+root.val
                p=(s-q)*q
                self.m=max(p,self.m)
                return q
        s=hs1(root)
        hs(root)
        return self.m%mod
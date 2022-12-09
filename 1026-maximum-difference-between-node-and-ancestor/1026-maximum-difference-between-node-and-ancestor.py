# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def hs(root,a,b):
            if(root==None):
                return
            self.ans=max(self.ans,abs(a-root.val),abs(b-root.val))
            a=max(a,root.val)
            b=min(b,root.val)
            hs(root.left,a,b)
            hs(root.right,a,b)
        hs(root,root.val,root.val)
        return self.ans
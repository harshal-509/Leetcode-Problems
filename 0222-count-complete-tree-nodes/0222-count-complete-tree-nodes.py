# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def hs(root):
            if(root==None):
                return
            else:
                self.ans+=1
                hs(root.left)
                hs(root.right)
        hs(root)
        return self.ans
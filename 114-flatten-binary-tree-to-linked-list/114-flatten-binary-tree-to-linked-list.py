# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(root):
            if(root==None):
                return
            solve(root.left)
            if(root.left):
                x=root.right
                root.right=root.left
                p=root.right
                root.left=None
                while(p.right!=None):
                    p=p.right
                p.right=x
            solve(root.right)
        solve(root)
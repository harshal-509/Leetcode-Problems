# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if(root.left==None and root.right==None):
                return root
            left=solve(root.left)
            right=solve(root.right)
            if(root.val==2):
                root.val=left.val | right.val
            else:
                root.val=left.val & right.val
            return root
        return solve(root).val
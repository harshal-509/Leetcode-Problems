# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if(root==None):
                return 0,-float('inf')
            left=solve(root.left)
            right=solve(root.right)
            return max(root.val,root.val+max(left[0],right[0])),max(root.val,left[1],right[1],root.val+max(left[0],right[0]),root.val+left[0]+right[0])     
        return solve(root)[1]
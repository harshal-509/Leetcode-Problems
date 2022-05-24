# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if(root==None):
                return [True,float('inf'),-float('inf')]
            left=solve(root.left)
            right=solve(root.right)
            if(root.val>left[2] and root.val<right[1] and left[0] and right[0]):
                return [True,min(root.val,left[1]),max(root.val,right[2])]
            return [False,-1,-1]
        return solve(root)[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i=0
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def solve(mi,ma):
            if(self.i>=n):
                return None
            if(preorder[self.i]<=ma and preorder[self.i]>=mi):
                root=TreeNode(preorder[self.i])
                self.i+=1
                root.left=solve(mi,min(ma,root.val))
                root.right=solve(max(mi,root.val),ma)
                return root
            return None
        n=len(preorder)
        return solve(-float('inf'),float('inf'))
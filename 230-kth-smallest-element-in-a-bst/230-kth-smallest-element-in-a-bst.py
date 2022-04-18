# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
        self.ans=-1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def solve(root):
            if(root!=None):
                solve(root.left)
                self.count+=1
                if(self.count==k):
                    self.ans=root.val 
                solve(root.right)
        solve(root)
        return self.ans
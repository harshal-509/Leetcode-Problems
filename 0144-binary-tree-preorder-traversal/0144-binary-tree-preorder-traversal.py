# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root):
            if(root!=None):
                self.ans.append(root.val)
                solve(root.left)
                solve(root.right)
        solve(root)
        return self.ans
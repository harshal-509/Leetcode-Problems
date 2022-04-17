# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr=None
    def increasingBST(self, root: TreeNode) -> TreeNode:
        global curr
        def solve(root):
            global curr
            if(root==None):
                return None
            solve(root.left)
            root.left=None
            curr.right=root
            curr=curr.right
            solve(root.right)
        ans=TreeNode(0)
        curr=ans
        solve(root)
        return ans.right
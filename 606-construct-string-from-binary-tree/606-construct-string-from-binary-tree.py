# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(root):
            if(root==None):
                return
            ans.append(str(root.val))
            if(root.left!=None or root.right!=None):
                ans.append("(")
            solve(root.left)
            if(root.left!=None or root.right!=None):
                if(root.right==None):
                    ans.append(")")
                else:
                    ans.append(")(")
            solve(root.right)
            if(root.left!=None or root.right!=None):
                if(root.right!=None):
                    ans.append(")")
        ans=[]
        solve(root)
        return "".join(ans)
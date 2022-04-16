# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.ri
x=0
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        global x
        def helper(root):
            global x
            if(root==None):
                return 0
            helper(root.right)
            z=root.val
            root.val+=x
            x+=z
            helper(root.left)
        x=0
        helper(root)
        return root
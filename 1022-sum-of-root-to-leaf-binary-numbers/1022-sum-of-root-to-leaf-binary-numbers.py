# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def traverse(node, s):
            if node:
                s += str(node.val)
                if node.left == None and node.right == None:
                    self.result += int(s, base=2)
                traverse(node.left, s)
                traverse(node.right, s)
        traverse(root, "")
        return self.result
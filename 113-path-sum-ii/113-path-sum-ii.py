# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root,targetSum):
    if(root==None):
        return []
    if(root.left==None and root.right==None):
        if(targetSum==root.val):
            return [[root.val]]
        else:
            return []
    a=helper(root.left,targetSum-root.val)+helper(root.right,targetSum-root.val)
    return [[root.val]+i for i in a]
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if(root==None):
            return []
        return helper(root,targetSum)
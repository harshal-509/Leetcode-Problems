# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans=[]
        def getNodes(root):
            if(root==None):
                return
            ans.append(root.val)
            getNodes(root.left)
            getNodes(root.right)
        getNodes(root1)
        getNodes(root2)
        ans.sort()
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def solve(root):
            if(root==None):
                return None
            if(root.left):
                if(root.left.val<low):
                    root.left.left=None
                    root.left=root.left.right
                    solve(root)
                else:
                    solve(root.left)
            if(root.right):
                if(root.right.val>high):
                    root.right.right=None
                    root.right=root.right.left
                    solve(root)
                else:
                    solve(root.right)
        def solve1(root):
            if(root):
                if(root.val>=low and root.val<=high):
                    return root
                if(root.val<low):
                    while(root and root.val<low):
                        root=root.right
                if(root.val>high):
                    while(root and root.val>high):
                        root=root.left
            else:
                return None
            return solve1(root)
        root=solve1(root)
        solve(root)
        return root
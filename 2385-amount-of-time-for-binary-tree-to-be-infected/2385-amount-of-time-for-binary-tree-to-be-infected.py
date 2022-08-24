# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        z=Counter()
        z1=Counter()
        def solve(root):
            if(root==None):
                return 0
            left=solve(root.left)
            right=solve(root.right)
            z[root.val]=(left,right)
            return max(left,right)+1
        def solve1(root):
            if(root==None):
                return [0,0]
            if(root.val==start):
                return [1,1]
            left=solve1(root.left)
            right=solve1(root.right)
            if(left[1]==0 and right[1]==0):
                return [max(left[0],right[0])+1,0]
            if(left[1]==0 and right[1]!=0):
                z1[root.val]=(left[0],right[0])
                return [right[0]+1,1]
            if(left[1]!=0 and right[1]==0):
                z1[root.val]=(left[0],right[0])
                return [left[0]+1,1]
        solve(root)
        solve1(root)
        ans=0
        ans=max(z[start])
        for i in z1:
            ans=max(ans,z1[i][0]+z1[i][1])
        return ans
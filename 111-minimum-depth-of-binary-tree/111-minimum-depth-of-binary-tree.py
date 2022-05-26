# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        q=deque([[root,1]])
        while(q):
            n=len(q)
            i=0
            while(i<n):
                x=q.popleft()
                if(not(x[0].left) and not(x[0].right)):
                    return x[1]
                if(x[0].left):
                    q.append([x[0].left,x[1]+1])
                if(x[0].right):
                    q.append([x[0].right,x[1]+1])
                i+=1
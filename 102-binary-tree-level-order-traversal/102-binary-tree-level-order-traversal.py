# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []
        q=deque([root])
        ans=[]
        while(q):
            temp=[]
            n=len(q)
            i=0
            while(i<n):
                x=q.popleft()
                if(x.left):
                    q.append(x.left)
                if(x.right):
                    q.append(x.right)
                temp.append(x.val)
                i+=1
            ans.append(temp)
        return ans
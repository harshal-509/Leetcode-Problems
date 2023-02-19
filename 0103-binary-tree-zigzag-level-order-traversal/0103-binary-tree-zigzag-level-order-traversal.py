# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []
        ans=[]
        q=deque([root])
        flag=0
        while(q):
            temp=deque([])
            n=len(q)
            i=0
            while(i<n):
                x=q.popleft()
                if(x.left):
                    q.append(x.left)
                if(x.right):
                    q.append(x.right)
                if(flag==0):
                    temp.append(x.val)
                else:
                    temp.appendleft(x.val)
                i+=1
            flag^=1
            ans.append(temp)
        return ans
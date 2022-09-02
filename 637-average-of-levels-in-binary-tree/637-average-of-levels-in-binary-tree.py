# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        z=defaultdict(list)
        q=deque([root])
        j=0
        while(q):
            t=len(q)
            i=0
            while(i<t):
                x=q.popleft()
                if(x.left):
                    q.append(x.left)
                if(x.right):
                    q.append(x.right)
                z[j].append(x.val)
                i+=1
            j+=1
        ans=[]
        for i in sorted(z.keys()):
            ans.append(sum(z[i])/len(z[i]))
        return ans
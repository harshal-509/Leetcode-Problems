# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root==None):
            return []
        q=deque([root])
        h=defaultdict(list)
        j=0
        while(q):
            n=len(q)
            i=0
            while(i<n):
                x=q.popleft()
                if(x.left):
                    q.append(x.left)
                if(x.right):
                    q.append(x.right)
                h[j].append(x.val)
                i+=1
            j+=1
        ans=[]
        for i in sorted(h.keys()):
            ans.append(h[i][-1])
        return ans
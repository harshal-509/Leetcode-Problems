# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        h=defaultdict(list)
        j=0
        while(q):
            n=len(q)
            i=0
            while(i<n):
                if(q[0].left):
                    q.append(q[0].left)
                if(q[0].right):
                    q.append(q[0].right)
                h[j].append(q[0].val)
                q.popleft()
                i+=1
            j+=1
        ans=[]
        k=sorted(h.keys(),reverse=True)
        return sum(h[k[0]])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(node):
            if node is None:
                return 0

            else:

                # Compute the depth of each subtree
                lDepth = maxDepth(node.left)
                rDepth = maxDepth(node.right)

                # Use the larger one
                if (lDepth > rDepth):
                    return lDepth+1
                else:
                    return rDepth+1
        z=Counter([])
        if(root==None):
            return 1
        q=deque([root])
        t=1
        p=maxDepth(root)
        while(q):
            temp=0
            n=len(q)
            i=0
            flag=0
            while(i<n):
                x=q.popleft()
                if(x.left):
                    if(flag==1):
                        return 0
                    q.append(x.left)
                else:
                    if(p-1==t):
                        flag=1
                if(x.right):
                    if(flag==1):
                        return 0        
                    q.append(x.right)
                else:
                    if(p-1==t):
                        flag=1
                temp+=1
                i+=1
            z[t]=temp
            t+=1
        for i in range(1,t-1):
            if(z[i]!=2**(i-1)):
                return 0
        return 1
        
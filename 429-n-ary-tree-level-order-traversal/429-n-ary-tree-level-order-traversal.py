"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(not(root)):
            return []
        else:
            ans=[]
            q=[root]
            l=[]
            count=0
            j=len(root.children)
            while(q):
                l=[]
                q1=[]
                for i in q:
                    l.append(i.val)
                    for j in i.children:
                        q1.append(j)
                ans.append(l)
                q=q1
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if(root==None):
            return "N"
        q=deque([root])
        ans=""
        while(q):
            n=len(q)
            i=0
            while(i<n):
                x=q.popleft()
                if(x!=None):
                    q.append(x.left)
                    q.append(x.right)
                if(x==None):
                    ans+="N "
                else:
                    ans+=str(x.val)+" "
                i+=1
        return ans

    def deserialize(self, s: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if(len(s)==0 or s[0]=="N"):           
            return None
        ip=list(map(str,s.split()))
        root=TreeNode(int(ip[0]))                     
        size=0
        q=deque()
        q.append(root)                            
        size=size+1 
        i=1                                       
        while(size>0 and i<len(ip)):
            currNode=q[0]
            q.popleft()
            size=size-1
            currVal=ip[i]
            if(currVal!="N"):
                currNode.left=TreeNode(int(currVal))
                q.append(currNode.left)
                size=size+1
            i=i+1
            if(i>=len(ip)):
                break
            currVal=ip[i]
            if(currVal!="N"):
                currNode.right=TreeNode(int(currVal))
                q.append(currNode.right)
                size=size+1
            i=i+1
        return root
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q=deque([root])
        ans=""
        while(q):
            t=q.popleft()
            if(t):
                ans+=str(t.val)+"$"
            else:
                ans+="#"+"$"
            if(t):
                q.append(t.left)
                q.append(t.right)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data=data.split("$")
        if(data[0]=="#"):
            return None
        root=TreeNode(int(data[0]))
        q=deque([root])
        i=1
        n=len(data)
        while(q):
            t=q.popleft()
            if(data[i]=="#"):
                t.left=None
            else:
                t.left=TreeNode(int(data[i]))
                q.append(t.left)
            i+=1
            if(data[i]=="#"):
                t.right=None
            else:
                t.right=TreeNode(int(data[i]))
                q.append(t.right)
            i+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
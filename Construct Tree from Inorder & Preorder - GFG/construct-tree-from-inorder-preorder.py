#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def __init__(self):
        self.i=0
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        def search(inorder,x):
            for i in range(len(inorder)):
                if(inorder[i]==x):
                    return i
        def create(inorder,preorder):
            if(len(inorder)==0 or self.i>=n):
                return None
            root=Node(preorder[self.i])
            m=search(inorder,preorder[self.i])
            self.i+=1
            root.left=create(inorder[:m],preorder)
            root.right=create(inorder[m+1:],preorder)
            return root
        n=len(inorder)
        return create(inorder,preorder)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends
#User function Template for python3

class Solution:
    def __init__(self):
        self.i=0
    def constructTree(self,post,n):
        # code here
        def solve(post,mi,ma):
            if(self.i<0):
                return None
            if(post[self.i]>=mi and post[self.i]<=ma):
                root=Node(post[self.i])
                self.i-=1
                root.right=solve(post,max(mi,root.val),ma)
                root.left=solve(post,mi,min(root.val,ma))
                return root
            return None
        self.i=n-1
        return solve(post,-float('inf'),float('inf'))
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
   def __init__(self,val):
       self.val=val
       self.left=None
       self.right=None
class BST:
   size=0
   def inorder(self,tmp,size=0):
       if tmp:
           self.inorder(tmp.left,self.size)
           print(tmp.val,end=" ")
           self.inorder(tmp.right,self.size)
     
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        obj=Solution()
        b=BST()
        pt=obj.constructTree(arr,n)
        b.inorder(pt)
        print()

# } Driver Code Ends
#User function Template for python3

#Function that constructs BST from its preorder traversal.
i=0
def post_order(pre,size):
    #code here
    global i
    i=0
    def solve(pre,mi,ma):
        global i
        if(i>=size):
            return None
        if(pre[i]>=mi and pre[i]<=ma):
            root=Node(pre[i])
            i+=1
            root.left=solve(pre,mi,min(root.data,ma))
            root.right=solve(pre,max(mi,root.data),ma)
            return root
        return None
    return solve(pre,-float('inf'),float('inf'))
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data,end=' ')

if __name__ == '__main__':
    t=int(input())

    for _tcs in range(t):
        size=int(input())
        pre=[int(x)for x in input().split()]

        root=post_order(pre,size)

        postOrd(root)
        print()
# } Driver Code Ends
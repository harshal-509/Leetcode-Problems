# Your task is to complete this function
# function should return true/false or 1/0
def isdeadEnd(root):
    # Code here
    def solve(root,mi,ma):
        if(root==None):
            return False
        left=solve(root.left,mi,min(root.data,ma))
        right=solve(root.right,max(root.data,mi),ma)
        if(left or right):
            return 1
        if(root and root.data==mi+1 and root.data==ma-1):
            return 1
        return 0
    return solve(root,0,float('inf'))
#{ 
#  Driver Code Starts
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        if isdeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
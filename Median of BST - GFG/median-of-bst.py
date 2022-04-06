#User function Template for python3
a=1
def findMedian(root):
    # code here
    # return the median
    global a
    def search(root,x):
        global a
        if(root==None):
            return None
        left=search(root.left,x)
        if(left!=None):
            return left
        if(a==x):
            return root.data
        a+=1
        right=search(root.right,x)
        if(right!=None):
            return right
    def countnodes(root):
        if(root==None):
            return 0
        return 1+countnodes(root.left)+countnodes(root.right)
    ans=countnodes(root)
    if(ans%2):
        a=1
        return search(root,ans//2+1)
    else:
        a=1
        x=search(root,ans//2)
        a=1
        y=search(root,ans//2+1)
        if((x+y)%2==0):
            return (x+y)//2
        return (x+y)/2
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(findMedian(root))

# } Driver Code Ends
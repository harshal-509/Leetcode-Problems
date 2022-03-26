#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        if(root==None):
            return []
        def leftboundary(root):
            q=deque([root])
            while(q):
                n=len(q)
                ans.append(q[0].data)
                for i in range(n):
                    x=q.popleft()
                    if(x.left):
                        q.append(x.left)
                    if(x.right):
                        q.append(x.right)
            ans.pop()
        def leafboundary(root):
            if(root==None):
                return
            if(root.left==None and root.right==None):
                ans.append(root.data)
            leafboundary(root.left)
            leafboundary(root.right)
        def rightboundary(root):
            q=deque([root])
            t=[]
            while(q):
                n=len(q)
                t.append(q[-1].data)
                if(q[-1].left==None and q[-1].right==None):
                    break
                for i in range(n):
                    x=q.popleft()
                    if(x.left):
                        q.append(x.left)
                    if(x.right):
                        q.append(x.right)
            if(t):
                t.pop()
            while(t):
                ans.append(t.pop())
        ans=[root.data]
        if(root.left==None and root.right==None):
            return ans
        if(root.left):
            leftboundary(root.left)
        leafboundary(root)
        if(root.right):
            rightboundary(root.right)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
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
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends
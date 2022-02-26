#User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        def merge(left,right):
            ans=Node(-1)
            temp=ans
            while(left!=None and right!=None):
                if(left.data<=right.data):
                    ans.next=Node(left.data)
                    left=left.next
                    ans=ans.next
                else:
                    ans.next=Node(right.data)
                    right=right.next
                    ans=ans.next
            while(left!=None):
                ans.next=Node(left.data)
                left=left.next
                ans=ans.next
            while(right!=None):
                ans.next=Node(right.data)
                right=right.next
                ans=ans.next
            return temp.next
        def hs(arr):
            if(len(arr)==1):
                return arr[0]
            n=len(arr)
            mid=n//2
            left=hs(arr[:mid])
            right=hs(arr[mid:])
            left=merge(left,right)
            return left
        ans=Node(-1)
        return hs(arr)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends
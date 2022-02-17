#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
import sys
sys.setrecursionlimit(1000000)
class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        if(head==None):
            return None
        if(head.next==None):
            return head
        next=None
        curr=head
        prev=None
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
#{ 
#  Driver Code Starts
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends
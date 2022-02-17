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
        def printf(head):
            f=head
            while(f!=None):
                print(f.data,end=" ")
                f=f.next
        def hs(head):
            if(head==None or head.next==None):
                return head
            res=hs(head.next)
            head.next.next=head
            head.next=None
            return res
        return hs(head)
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
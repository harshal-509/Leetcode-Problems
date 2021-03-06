#User function Template for python3
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        def hs(head):
            if(head==None):
                return 1    
            p=hs(head.next)
            x=head.data
            head.data=(head.data+p)%10
            return (x+p)//10
        t=hs(head)
        if(t==1):
            temp=Node(1)
            temp.next=head
            head=temp
        return head
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends
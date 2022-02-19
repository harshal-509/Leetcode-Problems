#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        def reverse(head):
            curr=head
            next=None
            prev=None
            while(curr!=None):
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        first=reverse(first)
        second=reverse(second)
        ans=Node(-1)
        sol=ans
        carry=0
        while(first!=None and second!=None):
            val=(first.data+second.data+carry)%10
            carry=(first.data+second.data+carry)//10
            ans.next=Node(val)
            ans=ans.next
            first=first.next
            second=second.next
        while(first!=None):
            val=(first.data+carry)%10
            carry=(first.data+carry)//10
            ans.next=Node(val)
            ans=ans.next
            first=first.next
        while(second!=None):
            val=(second.data+carry)%10
            carry=(second.data+carry)//10
            ans.next=Node(val)
            ans=ans.next
            second=second.next
        if(carry):
            ans.next=Node(1)
        sol=sol.next
        sol=reverse(sol)
        return sol
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
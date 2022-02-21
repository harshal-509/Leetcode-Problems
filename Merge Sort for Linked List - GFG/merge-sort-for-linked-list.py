#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        def merge(left,right):
            head=Node(-1)
            temp=head
            while(left!=None and right!=None):
                if(left.data<=right.data):
                    head.next=Node(left.data)
                    head=head.next
                    left=left.next
                else:
                    head.next=Node(right.data)
                    head=head.next
                    right=right.next
            while(left!=None):
                head.next=Node(left.data)
                head=head.next
                left=left.next
            while(right!=None):
                head.next=Node(right.data)
                head=head.next
                right=right.next
            return temp.next
        def getmid(head):
            slow=head
            fast=head.next
            while(fast!=None and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
            return slow
        def printf(head):
            temp=head
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            print("")
        def mergesort(head):
            if(head==None or head.next==None):
                return head
            mid=getmid(head)
            left=head
            right=mid.next
            mid.next=None
            left=mergesort(left)
            right=mergesort(right)
            left=merge(left,right)
            return left
        return mergesort(head)
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends
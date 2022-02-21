#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        def printf(head):
            temp=head
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            print("")
        def get(head):
            slow=head
            fast=head
            while(fast!=None and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
            return slow
        def reverse(head):
            curr=head
            prev=None
            next=None
            while(curr!=None):
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        mid=get(head)
        head1=mid
        head1=reverse(head1)
        while(head!=None and head1!=None):
            if(head.data!=head1.data):
                return 0
            head=head.next
            head1=head1.next
        return 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

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
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends
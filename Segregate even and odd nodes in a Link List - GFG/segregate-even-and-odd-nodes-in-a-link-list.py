# User function Template for Python3

# Following is the structure of node 
# class Node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, N, head):
        # code here
        def delete(par,head):
            if(par==None):
                x=head.data
                head=head.next
                return x,head
            x=head.data
            par.next=head.next
            return x,par.next
        def insertinbetween(temp,x):
            curr=temp.next
            new=node()
            new.data=x
            temp.next=new
            new.next=curr
        temp=None
        temp1=head
        while(temp1):
            if(temp1.data%2==0):
                temp=temp1
            temp1=temp1.next
        if(temp==None):
            return head
        temp1=head
        temp2=None
        temp3=temp
        while(temp1!=temp3):
            if(temp1.data%2):
                x,temp1=delete(temp2,temp1)
                if(temp2==None):
                    head=head.next
                insertinbetween(temp,x)
                temp=temp.next
            else:
                temp2=temp1
                temp1=temp1.next
        return head
#{ 
#  Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        newhead = ob.divide(n, list1.head)
        printlist(newhead)


# } Driver Code Ends
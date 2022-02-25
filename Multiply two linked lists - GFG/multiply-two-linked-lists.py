MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def multiplyTwoList(head1, head2):
    # Code here
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
    def num(head):
        ans=0
        i=0
        while(head):
            x=head.data
            ans+=pow(10,i)*x
            head=head.next
            i+=1
        return ans
    head1=reverse(head1)
    head2=reverse(head2)
    num1=num(head1)
    num2=num(head2)
    return ((num1*num2)%(int(1e9+7)))
#{ 
#  Driver Code Starts
class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(ptr):
    while ptr!=None:
        print(ptr.data, end=" ")
        ptr= ptr.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        # printlist(list1.get_head())
        # print ''
        list2 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list2.insert(i)
        # printlist(list2.get_head())
        # print ''
        print(multiplyTwoList(list1.get_head(), list2.get_head()))

# } Driver Code Ends
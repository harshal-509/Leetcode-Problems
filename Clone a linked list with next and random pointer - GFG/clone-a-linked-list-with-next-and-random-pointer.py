#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        def printf(head):
            temp=head
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
            print("")
        ans=Node(-1)
        ans1=ans
        temp=head
        while(temp!=None):
            ans.next=Node(temp.data)
            ans=ans.next
            temp=temp.next
        ans1=ans1.next
        temp=head
        temp1=ans1
        while(temp!=None and temp1!=None):
            next=temp.next
            temp.next=temp1
            temp=next
            next=temp1.next
            temp1.next=temp
            temp1=next
        temp=head
        while(temp!=None):
            if(temp.next):
                if(temp.arb):
                    temp.next.arb=temp.arb.next
                else:
                    temp.next.arb=temp.arb
            temp=temp.next.next
        temp=head
        temp1=ans1
        while(temp!=None and temp1!=None):
            temp.next=temp1.next
            temp=temp.next
            if(temp!=None):
                temp1.next=temp.next
            temp1=temp1.next
        return ans1
#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next
    

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    headp = head
    resp = res
    
    d = {}
    
    while head and res:
        if head==res:
            return
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        if head not in d:
            d[head] = res
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    head = headp
    res = resp
    while head:
        if head == res:
            return 
        if head.arb:
            if head.arb not in d:
                return
            if d[head.arb] != res.arb:
                return
        head=head.next
        res=res.next
        
    return True


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        __n,__m = list(map(int, input().strip().split()))
        __nodes = list(map(int, input().strip().split()))
        __aarb = list(map(int, input().strip().split()))
        __ll=LinkedList()
        __ll2=LinkedList()
        __ll.head=Node(__nodes[0])
        __ll2.head=Node(__nodes[0])
        __tail=__ll.head
        __tail2=__ll2.head
        
        for x in __nodes[1:]:
            __tail=insert(__tail,x)
            __tail2=insert(__tail2,x)
        
        for i in range(0,len(__aarb),2):
            setarb(__ll.head,__aarb[i],__aarb[i+1])
            setarb(__ll2.head,__aarb[i],__aarb[i+1])
        
        obj = Solution()
        __res=obj.copyList(__ll.head)
        if validation(__ll.head,__res) and validation(__ll2.head,__res):
            print(1)
        else:
            print(0)
# } Driver Code Ends
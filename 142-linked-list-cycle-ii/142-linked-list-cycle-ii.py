# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        x=head
        y=head
        print(y)
        while(x!=None and y!=None and y.next!=None):
            x=x.next
            y=y.next.next
            if(x==y):
                break
        if(x==None or y==None or y.next==None):
            return
        x=head
        while(x!=None and y!=None):
            if(x==y):
                return x
            x=x.next
            y=y.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        x=head
        y=head.next
        z=y
        while(x.next!=None and y.next!=None):
            x.next=x.next.next
            y.next=y.next.next
            x=x.next
            y=y.next
        x.next=z
        return head
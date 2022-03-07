# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        x=l1
        y=l2
        z=ListNode()
        head=z
        while(x!=None and y!=None):
            if(x.val<=y.val):
                z.next=ListNode(x.val)
                x=x.next
            else:
                z.next=ListNode(y.val)
                y=y.next
            z=z.next
        while(x!=None):
            z.next=ListNode(x.val)
            z=z.next
            x=x.next
        while(y!=None):
            z.next=ListNode(y.val)
            y=y.next
            z=z.next
        return head.next
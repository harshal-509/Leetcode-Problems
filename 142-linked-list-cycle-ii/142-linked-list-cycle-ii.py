# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def isloop(head):
            slow=head
            fast=head
            while(fast!=None):
                slow=slow.next
                if(fast.next==None):
                    break
                fast=fast.next.next
                if(slow==fast):
                    return fast
            return 0
        def starting(head,fast):
            slow=head
            curr=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return fast
        fast=isloop(head)
        if(fast==0):
            return 
        else:
            return starting(head,fast)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None):
            return 0
        slow=head
        fast=head.next
        while(fast!=None and fast.next!=None):
            if(slow==fast):
                return 1
            slow=slow.next
            fast=fast.next.next
        return 0
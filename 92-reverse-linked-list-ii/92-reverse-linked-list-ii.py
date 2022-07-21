# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l,i=0,0
        p=dummy
        while(i<=right):
            if(i==left-1):l=p
            if(i>left):
                pre.next = p.next
                tmp = l.next
                l.next = p
                p.next= tmp
                p=pre
            pre = p
            p=p.next
            i+=1
        return dummy.next
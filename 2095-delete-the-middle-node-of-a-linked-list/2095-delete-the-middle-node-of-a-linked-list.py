# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        y=0
        while(x!=None):
            x=x.next
            y+=1
        x=head
        pos=0
        if(y==1):
            return None
        while(pos!=(y//2)):
            pos+=1
            z=x
            x=x.next
        z.next=z.next.next
        return head
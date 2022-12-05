# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i=head
        j=head
        while(j!=None and j.next!=None):
            i=i.next
            j=j.next.next
        return i
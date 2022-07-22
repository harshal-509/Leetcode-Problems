# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a=ListNode(-1)
        ans=a
        b=ListNode(-1)
        ans1=b
        temp=head
        while(temp!=None):
            if(temp.val<x):
                a.next=ListNode(temp.val)
                a=a.next
            else:
                b.next=ListNode(temp.val)
                b=b.next
            temp=temp.next
        a.next=ans1.next
        return ans.next
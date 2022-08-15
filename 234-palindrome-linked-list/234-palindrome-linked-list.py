# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            curr=head
            temp=head
            prev=None
            while(curr!=None):
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        temp=head
        temp1=ListNode(-1)
        temp2=temp1
        while(temp!=None):
            temp1.next=ListNode(temp.val)
            temp1=temp1.next
            temp=temp.next
        head=reverse(head)
        temp1=temp2.next
        while(temp1!=None):
            if(temp1.val!=head.val):
                return 0
            temp1=temp1.next
            head=head.next
        return 1
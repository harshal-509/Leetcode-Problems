# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(head):
            print(head)
            if(head==None):
                return None
            if(head.next==None):
                return head
            temp=head.next
            temp1=temp.next
            temp.next=head
            head.next=swap(temp1)
            return temp
        return swap(head)
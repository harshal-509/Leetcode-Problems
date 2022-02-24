# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(left,mid,right):
            temp=ListNode(-1)
            temp1=temp
            while(left!=None and right!=None):
                if(left.val<=right.val):
                    temp.next=ListNode(left.val)
                    left=left.next
                    temp=temp.next
                else:
                    temp.next=ListNode(right.val)
                    right=right.next
                    temp=temp.next
            while(left!=None):
                temp.next=ListNode(left.val)
                left=left.next
                temp=temp.next
            while(right!=None):
                temp.next=ListNode(right.val)
                right=right.next
                temp=temp.next
            return temp1.next
        def getmid(head):
            slow=head
            fast=head.next
            while(fast!=None and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
            return slow
        def mergesort(head):
            if(head==None or head.next==None):
                return head
            mid=getmid(head)
            left=head
            right=mid.next
            mid.next=None
            left=mergesort(left)
            right=mergesort(right)
            left=merge(left,mid,right)
            return left
        return mergesort(head)
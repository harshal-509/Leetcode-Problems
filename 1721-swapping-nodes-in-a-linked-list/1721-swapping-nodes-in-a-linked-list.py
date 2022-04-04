# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def s(head):
            temp=head
            ans=0
            while(temp!=None):
                ans+=1
                temp=temp.next
            return ans
        if(head==None or head.next==None):
            return head
        if(k==1 or s(head)==k):
            temp=head
            k=1
            i=1
            while(i<k):
                temp=temp.next
                i+=1
            temp1=head
            second=temp1
            while(temp.next!=None):
                second=temp1
                temp1=temp1.next
                temp=temp.next
            if(head==second):
                temp=head
                head=second.next
                head.next=temp
                head.next.next=None
            else:
                temp=head.next
                temp1=head
                head=second.next
                head.next=temp
                second.next=temp1
                second.next.next=None
        else:
            first=head
            t=k
            c=1
            while(c<k-1):
                first=first.next
                c+=1
            temp=head
            i=1
            while(i<k):
                temp=temp.next
                i+=1
            temp1=head
            second=temp1
            while(temp.next!=None):
                second=temp1
                temp1=temp1.next
                temp=temp.next
            if(first.next==second):
                first.next=second.next
                second.next=second.next.next
                first.next.next=second
            else:
                temp=first.next.next
                temp1=first.next
                first.next=second.next
                temp2=second.next.next
                first.next.next=temp
                second.next=temp1
                second.next.next=temp2
        return head
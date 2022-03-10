# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        m=0
        s=0
        res=None
        ans=None
        i=l1
        j=l2
        while(j!=None and i!=None):
            s=i.val+j.val
            k=s
            new=ListNode((k+m)%10)
            if(res==None):
                res=new
                ans=new
            else:
                ans.next=new
                ans=new
            m=(k+m)//10
            i=i.next
            j=j.next
        if(i!=None):
            while(i!=None):
                s=i.val
                k=s
                new=ListNode((k+m)%10)
                ans.next=new
                ans=new
                m=(k+m)//10
                i=i.next
        else:
            while(j!=None):
                s=j.val
                k=s
                new=ListNode((k+m)%10)
                ans.next=new
                ans=new
                m=((k+m))//10
                j=j.next
        if(m!=0):
            new=ListNode(m)
            ans.next=new
            ans=new
        return res
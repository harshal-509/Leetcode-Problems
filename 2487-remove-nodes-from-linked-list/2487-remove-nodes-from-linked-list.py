# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=[]
        temp=head
        while(temp!=None):
            s.append(temp.val)
            temp=temp.next
        a=[0 for i in range(len(s))]
        t=0
        for i in range(len(s)-1,-1,-1):
            t=max(t,s[i])
            a[i]=t
        ans=ListNode(-1)
        sol=ans
        for i in range(len(s)):
            if(s[i]==a[i]):
                ans.next=ListNode(s[i])
                ans=ans.next
        return sol.next
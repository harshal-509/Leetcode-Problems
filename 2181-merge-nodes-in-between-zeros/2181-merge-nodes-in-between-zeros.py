# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        answer = ListNode(0)
        sol=answer
        while(temp!=None):
            temp1=temp.next
            val=0
            while(temp1 and temp1.val!=0):
                val+=temp1.val
                temp1=temp1.next
            temp=temp1
            if(val):
                node = ListNode(val)
                answer.next=node
                answer=answer.next
        return sol.next
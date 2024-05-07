# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if head is None or head.next is None:
                return head
            rest = reverse(head.next)
            head.next.next = head
            head.next = None
            return rest
        carry = 0
        head = reverse(head)
        answer= ListNode()
        solution = answer
        while(head!=None):
            val = head.val *2
            temp = (val+carry) % 10
            carry = (val+carry) // 10
            answer.next=ListNode(temp)
            answer=answer.next
            head=head.next
        if(carry):
            answer.next=ListNode(1)
        solution = reverse(solution.next)
        return solution
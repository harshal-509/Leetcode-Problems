# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        dummyPtr = dummy
        
        while dummyPtr.next and dummyPtr.next.next:
            currentVal = dummyPtr.next.val
            
            if dummyPtr.next.next.val == currentVal:
                while dummyPtr.next and dummyPtr.next.val == currentVal:
                    dummyPtr.next = dummyPtr.next.next
                continue
                    
            dummyPtr = dummyPtr.next
            
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        temp = head
        while(temp != None):
            temp = temp.next
            count = count + 1
        s = count % k
        t = count // k
        
        key = 0
        ans = []
        curr=head
        for i in range(k):
            temp = ListNode(-1)
            sol = temp
            p=0
            while(curr and p < t):
                temp.next = ListNode(curr.val)
                curr = curr.next
                temp = temp.next
                p+=1
            if(key<s and curr):
                temp.next = ListNode(curr.val)
                curr = curr.next
                temp = temp.next
                key+=1
            ans.append(sol.next)
        return ans
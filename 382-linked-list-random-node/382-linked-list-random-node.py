# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.l=[]
        self.n=0
        while(head):
            self.l.append(head.val)
            head=head.next
            self.n+=1
    def getRandom(self) -> int:
        return self.l[random.randrange(0,self.n)]
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
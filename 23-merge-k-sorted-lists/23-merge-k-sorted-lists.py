# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        r=[]
        def getList(head):
            res=[]
            while(head):
                res.append(head.val)
                head=head.next
            return res
        for i in lists:
            r= r+ getList(i)
        cur=ListNode(0)
        head=cur
        for i in sorted(r):
            head.next=ListNode(i)
            head=head.next
        return cur.next
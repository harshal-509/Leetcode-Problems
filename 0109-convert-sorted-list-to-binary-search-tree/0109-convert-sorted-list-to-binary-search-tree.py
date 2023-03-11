# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def middle(head):
            slow=head
            fast=head
            temp=None
            while(fast!=None and fast.next!=None):
                temp=slow
                slow=slow.next
                fast=fast.next.next
            return temp,slow
        def solve(head):
            if(head==None):
                return None
            if(head.next==None):
                return TreeNode(head.val)
            curr,mid=middle(head)
            prev=head
            next1=mid.next
            curr.next=None
            root=TreeNode(mid.val)
            root.left=solve(prev)
            root.right=solve(next1)
            return root
        return solve(head)
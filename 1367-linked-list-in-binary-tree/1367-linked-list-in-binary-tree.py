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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def solve(root,curr):
            if(curr==None):
                return 1
            if(root==None):
                return 0
            a=0
            if(root.val == curr.val):
                a = a | solve(root.left,curr.next)
                a = a | solve(root.right,curr.next)
            a = a | solve(root.left,head)
            a = a | solve(root.right,head)
            return a
        return solve(root,head)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        maxWidth = 0
        while queue:
            minLeft, maxRight = float('inf'), float('-inf')
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                minLeft = min(minLeft, idx)
                maxRight = max(maxRight, idx)
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
            maxWidth = max(maxWidth, maxRight - minLeft + 1)
                
        return maxWidth
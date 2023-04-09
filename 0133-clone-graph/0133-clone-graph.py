"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        new_map = {}
        def helper(cur):
            if cur.val in new_map:
                return new_map[cur.val]
            new_node = Node(cur.val, [])
            new_map[cur.val] = new_node
            for nei in cur.neighbors:
                new_node.neighbors.append(helper(nei))
            return new_node
        
        return helper(node)
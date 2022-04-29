class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node_from in range(len(graph)):
            if node_from not in colors and not self.bfs(graph, node_from, colors):
                return False
        return True

    def bfs(self, graph, node, colors):
        queue = deque([node])
        colors[node] = 1
        while queue:
            node_from = queue.popleft()
            for node_to in graph[node_from]:
                if node_to in colors:
                    if colors[node_to] == colors[node_from]:
                        return False
                else:
                    colors[node_to] = colors[node_from] * -1
                    queue.append(node_to)
        return True

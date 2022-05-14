class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for source, target, time in times:
            edges[source].append((time, target))
        dists = {}
        for i in range(1, n+1):
            dists[i] = float('inf')
        unvisited = [(0, k)]
        heapify(unvisited)
        visited = set()
        while len(unvisited) > 0:
            time, node = heappop(unvisited)
            if not node in visited:
                visited.add(node)
                dists[node] = time
                for target_time, target in edges[node]:
                    dists[target] = min(dists[target], time + target_time) 
                    heappush(unvisited, (dists[target], target))
        return max(dists.values()) if len(visited) == n else -1
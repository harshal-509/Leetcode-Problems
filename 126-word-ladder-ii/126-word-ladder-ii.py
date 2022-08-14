class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        lw = len(beginWord)
        variants: dict[str, list[str]] = defaultdict(list)
        for word in wordList:
            for i in range(lw):
                key = word[:i] + '*' + word[i + 1:]
                variants[key].append(word)
        q1: deque[str] = deque([beginWord])
        q2: deque[str] = deque([endWord]) 
        v1: set[str] = {beginWord} 
        v2: set[str] = {endWord}   
        found: bool = False
        graph: dict[str, set[str]] = defaultdict(set)
        def edge(src: str, dest: str, forward: bool) -> None:
            if forward:
                graph[src].add(dest)
            else:
                graph[dest].add(src)
        def bfs(q: deque[str], seen: set[str], opposing: set[str], forward: bool) -> None:
            nonlocal found
            lq = len(q)
            frontier: set[str] = set()
            for _ in range(lq):
                curr = q.popleft()
                for i in range(lw):
                    key = curr[:i] + '*' + curr[i + 1:]
                    for neigh in variants[key]:
                        if neigh in opposing:
                            edge(curr, neigh, forward)
                            found = True
                        elif neigh not in seen or neigh in frontier:
                            q.append(neigh)
                            edge(curr, neigh, forward)
                            seen.add(neigh)
                            frontier.add(neigh)
        while q1 and q2 and not found:
            if len(q1) <= len(q2):
                bfs(q1, v1, v2, forward=True)
            else:
                bfs(q2, v2, v1, forward=False)
        all_paths: list[list[str]] = []
        path: list[str] = [beginWord]
        def find_paths(curr: str) -> None:
            if curr == endWord:
                all_paths.append(path.copy())
                return
            for neigh in graph[curr]:
                path.append(neigh)
                find_paths(neigh)
                path.pop()
        find_paths(beginWord)
        return all_paths
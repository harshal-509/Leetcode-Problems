from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        check_word = set(wordList)
        if endWord not in check_word:
            return 0
        char = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        queue = deque([beginWord])
        res = 1
        visited = set()
        visited.add(beginWord)
        while queue:
            for _ in range(len(queue)):
                top = queue.popleft()
                if top==endWord:
                    return res
                for i in range(len(top)):
                    tmp = list(top)
                    for r in char:
                        tmp[i] = r
                        word = ''.join(tmp)
                        if word in check_word and word not in visited:
                            visited.add(word)
                            queue.append(word)
            res += 1
        if top!=endWord:
            return 0
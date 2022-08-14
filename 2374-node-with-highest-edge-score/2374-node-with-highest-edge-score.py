class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n=len(edges)
        e=[0 for i in range(n)]
        for i in range(n):
            e[edges[i]]+=i
        t=max(e)
        for i in range(n):
            if(t==e[i]):
                return i
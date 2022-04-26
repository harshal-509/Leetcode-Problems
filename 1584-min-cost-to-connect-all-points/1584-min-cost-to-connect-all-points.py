class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def minKey(key, mstSet):
            min = sys.maxsize
            min_index=-1
            for v in range(n):
                if key[v] < min and mstSet[v] == False:
                    min = key[v]
                    min_index = v
            return min_index
        def primMST():
            key = [sys.maxsize] *n
            parent = [None] * n
            key[0] = 0
            mstSet = [False] * n
            parent[0]=-1
            for cout in range(n):
                u = minKey(key, mstSet)
                mstSet[u] = True
                for v in range(n):
                    if(g[u][v] > 0 and mstSet[v] == False and key[v] > g[u][v]):
                            key[v] = g[u][v]
                            parent[v] = u
            ans=0
            for i in range(1,n):
                ans+=g[i][parent[i]]
            return ans
        n=len(points)
        g=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                g[i][j]=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        return primMST()
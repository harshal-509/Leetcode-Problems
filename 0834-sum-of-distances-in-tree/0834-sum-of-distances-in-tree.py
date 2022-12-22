class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count=[1]*n
        dist=[0]*n
        def createGraph():
            g=[[] for i in range(n)]
            for u,v in edges:
                g[u].append(v)
                g[v].append(u)
            return g
        g=createGraph()
        def postOrder(curr,parent):
            for it in g[curr]:
                if it!=parent:
                    postOrder(it,curr)
                    count[curr]+=count[it]
                    dist[curr]+=dist[it]+count[it]
            return
        def preOrder(curr,parent):
            for it in g[curr]:
                if it!=parent:
                    dist[it]=dist[curr]-count[it]+(n-count[it])
                    preOrder(it,curr)
            return
        postOrder(0,-1)
        preOrder(0,-1)
        return dist
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(s, e):
            z[s] = 1
            for u in d[s]:
                if u == e:
                    continue
                dfs(u, s)
                z[s] += z[u]
        d=defaultdict(list)
        n=len(roads)+1
        for i in roads:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        vis=[0 for i in range(n)]
        z = [0] * (n)
        dfs(0,0)
        ans=0
        for i in range(n):
            if(i!=0):
                if(z[i]%seats==0):
                    ans+=z[i]//seats
                else:
                    ans+=z[i]//seats+1
        return ans
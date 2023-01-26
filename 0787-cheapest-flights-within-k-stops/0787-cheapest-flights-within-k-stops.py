class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def dfs(i,des,k):
            if(i==des):
                return 0
            if((i,k) in z):
                return z[(i,k)]
            ans=float('inf')
            for j in d[i]:
                if(k):
                    ans=min(ans,dfs(j[0],des,k-1)+j[1])
            z[(i,k)]=ans
            return ans
        d=defaultdict(list)
        for i in flights:
            d[i[0]].append([i[1],i[2]])
        s=set()
        z=Counter([])
        x=dfs(src,dst,k+1)
        if(x==float('inf')):
            return -1
        return x
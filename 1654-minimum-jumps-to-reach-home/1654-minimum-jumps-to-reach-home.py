class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        z=Counter(forbidden)
        @cache
        def solve(i,temp):
            if(i<0 or z[i] or i>limit):
                return float('inf')
            if(i==x):
                return 0
            if(vis[i]==1):
                return float('inf')
            vis[i]=1
            a1=solve(i+a,0)+1
            b1=float('inf')
            if(temp!=1):
                b1=solve(i-b,1)+1
            vis[i]=0
            return min(a1,b1)
        limit=max(x, max(forbidden)) + a + b
        vis=Counter([])
        x=solve(0,0)
        if(x==float('inf')):
            return -1
        return x
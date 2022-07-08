class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def f(i,t,p):
            if i==m or t<0:
                return 0 if t==0 else inf
            ans=inf
            if houses[i]==0:
                for j in range(n):
                    ans=min(ans,cost[i][j]+f(i+1,t-(1 if p!=j+1 else 0),j+1))
            else:
                ans=min(ans,f(i+1,t-(1 if p!=houses[i] else 0),houses[i]))
            return ans
        a=f(0,target,-1)
        return a if a!=inf else -1
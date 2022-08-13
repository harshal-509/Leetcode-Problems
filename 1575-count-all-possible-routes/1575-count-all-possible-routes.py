class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def solve(i,f):
            if(f<0):
                return 0
            ans=0
            if(dp[i][f]!=-1):
                return dp[i][f]
            for j in range(n):
                if(i!=j and f-abs(locations[i]-locations[j])>=0):
                    ans+=solve(j,f-abs(locations[i]-locations[j]))
                    if(j==finish):
                        ans+=1
            dp[i][f]=ans
            return ans
        n=len(locations)
        mod=int(1e9+7)
        dp=[[-1 for i in range(fuel+1)] for j in range(n+1)]
        if(finish==start):
            return (solve(start,fuel)+1)%mod
        return solve(start,fuel)%mod
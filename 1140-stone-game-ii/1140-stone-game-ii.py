class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def solve(i,m):
            if(i>=n):
                return 0
            if(n-i<=2*m):
                return sum(piles[i:])
            if(dp[i][m]!=-1):
                return dp[i][m]
            s=0
            t=sum(piles[i:])
            for j in range(1,2*m+1):
                op=solve(i+j,max(m,j))
                s=max(s,t-op)
            dp[i][m]=s
            return s
        n=len(piles)
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        return solve(0,1)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def solve(i,j):
            if(j==m):
                return 1
            if(j>=m or i>=n):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            ans=0
            if(s[i]==t[j]):
                ans+=solve(i+1,j+1)
                ans+=solve(i+1,j)
            else:
                ans+=solve(i+1,j)
            dp[i][j]=ans
            return ans
        n=len(s)
        m=len(t)
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        return solve(0,0)
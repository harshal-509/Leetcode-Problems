class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        def solve(i,j):
            if(i>=n):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            a=solve(i+1,j+1)+satisfaction[i]*j
            b=solve(i+1,j)
            dp[i][j]=max(a,b)
            return max(a,b)
        n=len(satisfaction)
        dp=[[-1 for i in range(n+2)] for j in range(n+1)]
        return solve(0,1)
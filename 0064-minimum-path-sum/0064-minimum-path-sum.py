class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for i in range(m)] for j in range(n)]
        dp[n-1][m-1]=grid[n-1][m-1]
        for i in range(m-2,-1,-1):
            dp[n-1][i]=grid[n-1][i]+dp[n-1][i+1]
        for i in range(n-2,-1,-1):
            dp[i][m-1]=grid[i][m-1]+dp[i+1][m-1]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j][i]=grid[j][i]+min(dp[j+1][i],dp[j][i+1])
        return dp[0][0]
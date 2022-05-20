class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def valid(i,j):
            if(i>=0 and i<n and j>=0 and j<m and obstacleGrid[i][j]==0 and vis[i][j]==0):
                return 1
            return 0
        def solve(i,j):
            if(mem[i][j]!=-1):
                return mem[i][j]
            if(i==n-1 and j==m-1):
                return 1
            vis[i][j]=1
            a=0
            if(valid(i,j+1)):
                a+=solve(i,j+1)
            if(valid(i+1,j)):
                a+=solve(i+1,j)
            vis[i][j]=0
            mem[i][j]=a
            return a
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        mem=[[-1 for i in range(m)] for j in range(n)]
        if(obstacleGrid[0][0] or obstacleGrid[-1][-1]):
            return 0
        return solve(0,0)
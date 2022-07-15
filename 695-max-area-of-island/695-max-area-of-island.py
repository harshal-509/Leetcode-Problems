t=0
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            global t
            if(i>=n or i<=-1 or j>=m or j<=-1 or grid[i][j]==0):
                return
            else:
                t+=1
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return t
        n=len(grid)
        m=len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    global t
                    t=0
                    ans=max(ans,dfs(i,j))
        return ans
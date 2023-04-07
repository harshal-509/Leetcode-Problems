class Solution:
    def __init__(self):
        self.temp=0
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if(i<0 or j<0 or i>=n or j>=m):
                return 1
            if(vis[i][j]):
                return
            ans=0
            if(grid[i][j]):
                self.temp+=1
                vis[i][j]=1
                a=dfs(i+1,j)
                b=dfs(i-1,j)
                c=dfs(i,j-1)
                d=dfs(i,j+1)
                if(a or b or c or d):
                    ans=ans|1
                return ans
            else:
                return
        n=len(grid)
        m=len(grid[0])
        ans=0
        vis=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if(vis[i][j]==0 and grid[i][j]):
                    self.temp=0
                    x=dfs(i,j)
                    if(x):
                        pass
                    else:
                        ans+=self.temp
        return ans
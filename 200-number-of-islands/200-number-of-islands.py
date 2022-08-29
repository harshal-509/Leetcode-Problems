class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(i,j):
            if(i>=0 and i<n and j>=0 and j<m):
                return 1
            else:
                return 0
        def hs(i,j):
            grid[i][j]="0"
            if(valid(i-1,j) and grid[i-1][j]=="1"):
                hs(i-1,j)
            if(valid(i+1,j) and grid[i+1][j]=="1"):
                hs(i+1,j)
            if(valid(i,j+1) and grid[i][j+1]=="1"):
                hs(i,j+1)
            if(valid(i,j-1) and grid[i][j-1]=="1"):
                hs(i,j-1)
        n=len(grid)
        m=len(grid[0])
        ans=0
        for a in range(n):
            for b in range(m):
                if(grid[a][b]=="1"):
                    ans+=1
                    hs(a,b)
        return ans
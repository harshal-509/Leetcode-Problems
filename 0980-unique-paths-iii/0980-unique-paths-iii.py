class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def hs(i,j,z):
            if(i<0 or j<0 or i>=n or j>=m or grid[i][j]==-1):
                return 0
            if(grid[i][j]==2):
                if(z==-1):
                    return 1
                return 0
            grid[i][j]=-1
            z-=1
            ans=hs(i+1,j,z)+hs(i-1,j,z)+hs(i,j+1,z)+hs(i,j-1,z)
            grid[i][j]=0
            z+=1
            return ans
        n=len(grid)
        m=len(grid[0])
        z=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    a=i
                    b=j
                if(grid[i][j]==0):
                    z+=1
        return hs(a,b,z)
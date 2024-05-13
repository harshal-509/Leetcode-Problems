class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            if(grid[i][0]==0):
                for j in range(m):
                    grid[i][j]^=1
        for j in range(1,m):
            one=0
            zero=0
            for i in range(n):
                if(grid[i][j]==1):
                    one+=1
                else:
                    zero+=1
            if(one<zero):
                for i in range(n):
                    grid[i][j]^=1
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]):
                    ans+=1<<(m-j-1)
        return ans
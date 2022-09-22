class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        mat=[0 for i in range(m)]
        mat1=[0 for j in range(n)]
        for i in range(n):
            for j in range(m):
                if(grid[i][j]):
                    mat[j]+=1
                    mat1[i]+=1
        ans=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1 and (mat[j]>=2 or mat1[i]>=2)):
                    ans+=1
        return ans
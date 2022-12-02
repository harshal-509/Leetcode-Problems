class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        row=[[0,0] for i in range(n)]
        col=[[0,0] for i in range(m)]
        for i in range(n):
            a=0
            b=0
            for j in range(m):
                if(grid[i][j]==1):
                    a+=1
                else:
                    b+=1
            row[i][0]=a
            row[i][1]=b
        for i in range(m):
            a=0
            b=0
            for j in range(n):
                if(grid[j][i]==1):
                    a+=1
                else:
                    b+=1
            col[i][0]=a
            col[i][1]=b
        ans=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j]=row[i][0]+col[j][0]-row[i][1]-col[j][1]
        return ans
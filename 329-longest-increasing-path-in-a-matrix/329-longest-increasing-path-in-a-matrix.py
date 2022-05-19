class Solution:
    def __init__(self):
        self.ans=0
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def valid(a,b,c,d):
            if(c>=0 and c<n and d>=0 and d<m and vis[c][d]==0 and matrix[c][d]>matrix[a][b]):
                return 1
            return 0
        def solve(i,j):
            if(mem[i][j]!=-1):
                return mem[i][j]
            vis[i][j]=1
            a=0
            if(valid(i,j,i+1,j)):
                a=max(a,1+solve(i+1,j))
            if(valid(i,j,i-1,j)):
                a=max(a,1+solve(i-1,j))
            if(valid(i,j,i,j+1)):
                a=max(a,1+solve(i,j+1))
            if(valid(i,j,i,j-1)):
                a=max(a,1+solve(i,j-1))
            vis[i][j]=0
            mem[i][j]=a
            return a
        n=len(matrix)
        m=len(matrix[0])
        vis=[[0 for i in range(m)] for i in range(n)]
        mem=[[-1 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                x=solve(i,j)
                self.ans=max(self.ans,x+1)
        return self.ans
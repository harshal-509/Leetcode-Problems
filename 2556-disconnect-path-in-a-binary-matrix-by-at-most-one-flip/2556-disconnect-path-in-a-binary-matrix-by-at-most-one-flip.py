class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        def valid(i,j):
            if(i>=0 and i<n and j>=0 and j<m and grid[i][j]==1):
                return 1
            return 0
        def ispos(i,j):
            if(i==n-1 and j==m-1):
                return 1
            grid[i][j]=0
            if(valid(i+1,j)):
                if(ispos(i+1,j)):
                    return 1
            if(valid(i,j+1)):
                if(ispos(i,j+1)):
                    return 1
            return 0
        n=len(grid)
        m=len(grid[0])
#         for i in grid:
#             print(i)
#         if(n==1 and m==1):
#             return 0
#         if(n==1 and m==2):
#             return 0
#         if(n==2 and m==1):
#             return 0
#         if(n==1):
#             ans=1
#             x=grid[0][1]
#             grid[0][1]=0
#             vis=[[0 for i in range(m)] for j in range(n)]
#             ans&=ispos(0,0)
#             grid[0][1]=x
#             x=grid[-1][-2]
#             grid[-1][-2]=0
#             vis=[[0 for i in range(m)] for j in range(n)]
#             ans&=ispos(0,0)
#             return not(ans)
#         if(m==1):
#             ans=1
#             x=grid[1][0]
#             grid[1][0]=0
#             vis=[[0 for i in range(m)] for j in range(n)]
#             ans&=ispos(0,0)
#             grid[1][0]=x
#             x=grid[-2][-1]
#             grid[-2][-1]=0
#             vis=[[0 for i in range(m)] for j in range(n)]
#             ans&=ispos(0,0)
#             return not(ans)
#         vis=[[0 for i in range(m)] for j in range(n)]
#         x=grid[1][0]
#         grid[1][0]=0
#         ans=ispos(0,0)
#         grid[1][0]=x
#         x=grid[0][1]
#         grid[0][1]=0
#         vis=[[0 for i in range(m)] for j in range(n)]
#         ans&=ispos(0,0)
#         grid[0][1]=x
#         x=grid[-1][-2]
#         grid[-1][-2]=0
#         vis=[[0 for i in range(m)] for j in range(n)]
#         ans&=ispos(0,0)
#         grid[-1][-2]=x
#         x=grid[-2][-1]
#         grid[-2][-1]=0
#         vis=[[0 for i in range(m)] for j in range(n)]
#         ans&=ispos(0,0)
        
#         return not(ans)
        ans=ispos(0,0)
        if(ans==0):
            return 1
        ans=ispos(0,0)
        if(ans==0):
            return 1
        return 0
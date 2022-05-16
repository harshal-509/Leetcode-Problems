class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def valid(i,j):
            if(i>=0 and i<n and j>=0 and j<n and grid[i][j]==0 and vis[i][j]==0):
                return 1
            return 0
        n=len(grid)
        vis=[[0 for i in range(n)] for i in range(n)]
        if(grid[0][0]==1):
            return -1
        q=deque([[0,0]])
        j=1
        vis[0][0]=1
        while(q):
            p=len(q)
            i=0
            while(i<p):
                x=q[0][0]
                y=q[0][1]
                if(x==n-1 and y==n-1):
                    return j
                for a in range(x-1,x+2):
                    for b in range(y-1,y+2):
                        if(valid(a,b)):
                            q.append([a,b])
                            vis[a][b]=1
                q.popleft()
                i+=1
            j+=1
        return -1
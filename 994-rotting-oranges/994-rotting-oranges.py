class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def valid(i,j):
            if(i>=0 and i<n and j>=0 and j<m and vis[i][j]==0 and grid[i][j]==1):
                return 1
            return 0
        q=deque([])
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        p=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==2):
                    q.append([i,j,0])
                    vis[i][j]=1
                elif(grid[i][j]==1):
                    p+=1
        ans=0
        t=0
        while(q):
            x=q.popleft()
            if(grid[x[0]][x[1]]==1):
                t+=1
            ans=max(ans,x[2])
            if(valid(x[0]+1,x[1])):
                vis[x[0]+1][x[1]]=1
                q.append([x[0]+1,x[1],x[2]+1])
            if(valid(x[0]-1,x[1])):
                vis[x[0]-1][x[1]]=1
                q.append([x[0]-1,x[1],x[2]+1])
            if(valid(x[0],x[1]+1)):
                vis[x[0]][x[1]+1]=1
                q.append([x[0],x[1]+1,x[2]+1])
            if(valid(x[0],x[1]-1)):
                vis[x[0]][x[1]-1]=1
                q.append([x[0],x[1]-1,x[2]+1])
        if(t<p):
            return -1
        return ans
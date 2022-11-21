class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(x,y):
            if(x>=0 and x<n and y<m and y>=0 and vis[x][y]==0 and maze[x][y]=='.'):
                return 1
            return 0
        n=len(maze)
        m=len(maze[0])
        q=deque([[entrance[0],entrance[1],0]])
        vis=[[0 for i in range(m)] for j in range(n)]
        vis[entrance[0]][entrance[1]]=1
        while(q):
            x,y,s=q.popleft()
            if((x==0 or x==n-1 or y==0 or y==m-1) and s!=0):
                return s
            if(valid(x+1,y)):
                q.append([x+1,y,s+1])
                vis[x+1][y]=1
            if(valid(x-1,y)):
                q.append([x-1,y,s+1])
                vis[x-1][y]=1
            if(valid(x,y+1)):
                q.append([x,y+1,s+1])
                vis[x][y+1]=1
            if(valid(x,y-1)):
                q.append([x,y-1,s+1])
                vis[x][y-1]=1
        return -1
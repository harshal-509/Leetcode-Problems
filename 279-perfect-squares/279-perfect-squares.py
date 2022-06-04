class Solution:
    def numSquares(self, n: int) -> int:
        ans=[]
        for i in range(101):
            ans.append(i*i)
        q=deque([[0,0]])
        vis=Counter([])
        while(q):
            t=q.popleft()
            if(t[0]==n):
                return t[1]
            for i in range(100,0,-1):
                if(t[0]+ans[i]<=n):
                    if(vis[tuple([t[0]+ans[i],t[1]+1])]==0):
                        q.append([t[0]+ans[i],t[1]+1])
                        vis[tuple([t[0]+ans[i],t[1]+1])]=1
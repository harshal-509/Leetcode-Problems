class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # dfs TLE
        # def dfs(i,f,c):
        #     if(i==f):
        #         return 0
        #     ans=float('inf')
        #     for j in d[i]:
        #         if(vis[j[0]][j[1]]==0):
        #             if(j[1]!=c):
        #                 vis[j[0]][j[1]]=1
        #                 ans=min(ans,dfs(j[0],f,j[1])+1)
        #                 vis[j[0]][j[1]]=0
        #     return ans
        # d=defaultdict(list)
        # for i in redEdges:
        #     d[i[0]].append([i[1],0])
        # for i in blueEdges:
        #     d[i[0]].append([i[1],1])
        # ans=[]
        # for i in range(n):
        #     vis=[[0,0] for i in range(n)]
        #     vis[0][1]=1
        #     x=dfs(0,i,1)
        #     vis=[[0,0] for i in range(n)]
        #     vis[0][0]=1
        #     y=dfs(0,i,0)
        #     if(x==float('inf') and y==float('inf')):
        #         ans.append(-1)
        #     else:
        #         ans.append(min(x,y))
        # return ans
        d=defaultdict(list)
        for i in redEdges:
            d[i[0]].append([i[1],0])
        for i in blueEdges:
            d[i[0]].append([i[1],1])
        ans2=[]
        for i in range(n):
            vis=[[0,0] for k in range(n)]
            vis[0][0]=1
            q=deque([[0,0,0]])
            ans=-1
            while(q):
                t=q.popleft()
                if(t[0]==i):
                    ans=t[2]
                    break
                for j in d[t[0]]:
                    if(vis[j[0]][j[1]]==0):
                        if(j[1]!=t[1]):
                            vis[j[0]][j[1]]=1
                            q.append([j[0],j[1],t[2]+1])
                        
            vis=[[0,0] for k in range(n)]
            vis[0][1]=1
            q=deque([[0,1,0]])
            ans1=-1
            while(q):
                t=q.popleft()
                if(t[0]==i):
                    ans1=t[2]
                    break
                for j in d[t[0]]:
                    if(vis[j[0]][j[1]]==0):
                        if(j[1]!=t[1]):
                            vis[j[0]][j[1]]=1
                            q.append([j[0],j[1],t[2]+1])
            
            if(ans==-1 and ans1==-1):
                ans2.append(-1)
            else:
                if(ans==-1):
                    ans2.append(ans1)
                elif(ans1==-1):
                    ans2.append(ans)
                else:
                    ans2.append(min(ans,ans1))
        return ans2
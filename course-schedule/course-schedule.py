class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def hs(g,ans):
            q=deque([])
            for i in range(n):
                if(ind[i]==0):
                    q.append(i)
            while(len(q)):
                x=q.popleft()
                ans.append(x)
                for j in g[x]:
                    ind[j]-=1
                    if(ind[j]==0):
                        q.append(j)
        n=numCourses
        g=[[] for i in range(n)]
        ind=[0 for i in range(n)]
        v=[0 for i in range(n)]
        for i in prerequisites:
            g[i[1]].append(i[0])
            ind[i[0]]+=1
        ans=[]
        hs(g,ans)
        return len(ans)==n
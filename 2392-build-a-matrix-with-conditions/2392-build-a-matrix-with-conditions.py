class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ind=[0 for i in range(k+1)]
        ind1=[0 for i in range(k+1)]
        ans=[[0 for i in range(k)] for j in range(k)]
        d=defaultdict(list)
        d1=defaultdict(list)
        for i in rowConditions:
            d[i[0]].append(i[1])
            ind[i[1]]+=1
        for i in colConditions:
            d1[i[0]].append(i[1])
            ind1[i[1]]+=1
        q=deque([])
        q1=deque([])
        z=Counter([])
        z1=Counter([])
        for i in range(1,k+1):
            if(ind[i]==0):
                q.append(i)
            if(ind1[i]==0):
                q1.append(i)
        p=0
        while(q):
            x=q.popleft()
            z[x]=p
            for j in d[x]:
                ind[j]-=1
                if(ind[j]==0):
                    q.append(j)
            p+=1
        p=0
        while(q1):
            x=q1.popleft()
            z1[x]=p
            for j in d1[x]:
                ind1[j]-=1
                if(ind1[j]==0):
                    q1.append(j)
            p+=1
        if(len(z)==k and len(z1)==k):
            for i in range(1,k+1):
                a=z[i]
                b=z1[i]
                ans[a][b]=i
            return ans
        return []
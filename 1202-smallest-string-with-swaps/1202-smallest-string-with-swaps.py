class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i,temp,vis):
            vis[i]=1
            temp.append(i)
            temp1.append(s[i])
            for j in d[i]:
                if(vis[j]==0):
                    dfs(j,temp,vis)
        d=defaultdict(list)
        n=len(s)
        m=len(pairs)
        for i in range(m):
            d[pairs[i][0]].append(pairs[i][1])
            d[pairs[i][1]].append(pairs[i][0])
        ap=[]
        jp=[]
        vis=[0 for i in range(n)]
        for i in range(n):
            temp=[]
            temp1=[]
            if(vis[i]==0):
                dfs(i,temp,vis)
            if(temp):
                ap.append(temp.copy())
                jp.append(temp1.copy())
        for i in jp:
            i.sort()
        for i in ap:
            i.sort()
        h={}
        m=len(ap)
        for i in range(m):
            for j in range(len(ap[i])):
                h[ap[i][j]]=jp[i][j]
        ans=""
        for i in range(n):
            ans+=h[i]
        return ans
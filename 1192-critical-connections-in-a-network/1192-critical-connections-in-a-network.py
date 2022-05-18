timer=0
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        global timer
        def dfs(ch):
            global timer
            dic[ch]=timer
            low[ch]=timer
            vis[ch]=1
            timer+=1
            for j in d[ch]:
                if(vis[j]==0):
                    par[j]=ch
                    dfs(j)
                    low[ch]=min(low[ch],low[j])
                    if(low[j]>dic[ch]):
                        ans.append([ch,j])
                else:
                    if(j!=par[ch]):
                        low[ch]=min(low[ch],dic[j])
        d=defaultdict(list)
        for i in connections:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        dic=[-1 for i in range(n)]
        low=[-1 for i in range(n)]
        vis=[0 for i in range(n)]
        par=[-1 for i in range(n)]
        ans=[]
        ans=[]
        dfs(0)
        return ans
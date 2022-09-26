class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def find(x):
            if(x==par[x]):
                return x
            par[x]=find(par[x])
            return par[x]
        n=len(vals)
        par=[i for i in range(n)]
        c=[1 for i in range(n)]
        edges.sort(key=lambda x:max(vals[x[0]],vals[x[1]]))
        ans=0
        for i in edges:
            a=find(i[0])
            b=find(i[1])
            if(vals[a]==vals[b]):
                ans+=c[a]*c[b]
                par[a]=b
                c[b]+=c[a]
            else:
                if(vals[a]<vals[b]):
                    par[a]=b
                else:
                    par[b]=a
        return ans+n
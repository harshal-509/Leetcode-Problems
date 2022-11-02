class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def check(x,y):
            t=0
            for i in range(len(x)):
                if(x[i]!=y[i]):
                    t+=1
            return t==1
        def solve(x):
            if(x==end):
                return 0
            ans=float('inf')
            for j in range(n):
                if(vis[j]==0 and check(x,bank[j])):
                    vis[j]=1
                    ans=min(ans,solve(bank[j])+1)
                    vis[j]=0
            return ans
        n=len(bank)
        vis=[0 for i in range(n)]
        x=solve(start)
        if(x==float('inf')):
            return -1
        return x
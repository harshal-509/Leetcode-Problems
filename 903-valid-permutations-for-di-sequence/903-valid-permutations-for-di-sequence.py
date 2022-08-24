class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n=len(s)+1
        def solve(i,j):
            if(j>=n-1):
                return 1
            if(dp[i][j]!=-1):
                return dp[i][j]
            ans=0
            if(s[j]=="D"):
                for k in range(i-1,-1,-1):
                    if(vis[k]==0):
                        vis[k]=1
                        ans+=solve(k,j+1)
                        vis[k]=0
            else:
                for k in range(i+1,n):
                    if(vis[k]==0):
                        vis[k]=1
                        ans+=solve(k,j+1)
                        vis[k]=0
            dp[i][j]=ans
            return ans
        ans=0
        vis=[0 for i in range(n)]
        dp=[[-1 for i in range(n-1)] for j in range(n)]
        for i in range(n):
            vis[i]=1
            ans+=solve(i,0)
            vis[i]=0
        return ans%(int(1e9+7))
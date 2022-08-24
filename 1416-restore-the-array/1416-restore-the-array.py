class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # Top-Down --MLE
        # def solve(i):
        #     if(i>=n):
        #         return 0
        #     ans=0
        #     if(dp[i]!=-1):
        #         return dp[i]
        #     for j in range(i+1,min(i+1+t,n+1)):
        #         x=int(s[i:j])
        #         if(j==n):
        #             if(x<=k and x>=1):
        #                 ans+=1
        #             return ans
        #         if(x<=k and x>=1):
        #             ans+=solve(j)
        #         else:
        #             break
        #     dp[i]=ans
        #     return ans
        # n=len(s)
        # t=len(str(k))+1
        # dp=[-1 for i in range(n+1)]
        # return solve(0)%(int(1e9+7))
        
        
        # BOTTOM-UP 
        n=len(s)
        dp=[0 for i in range(n+1)]
        t=len(str(k))+1
        for i in range(n-1,-1,-1):
            ans=0
            for j in range(i+1,min(i+1+t,n+1)):
                x=int(s[i:j])
                if(j==n):
                    if(x<=k and x>=1):
                        ans+=1
                if(x<=k and x>=1):
                    ans+=dp[j]
                else:
                    break
            dp[i]=ans
        return dp[0]%(int(1e9+7))
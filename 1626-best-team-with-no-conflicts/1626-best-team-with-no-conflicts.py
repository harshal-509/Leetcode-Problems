class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # memoization - TLE
        # def solve(i,temp):
        #     if(i>=n):
        #         return 0
        #     a=0
        #     if(dp[i][temp]!=-1):
        #         return dp[i][temp]
        #     if(temp==-1 or z[temp][1]<=z[i][1]):
        #         a=solve(i+1,i)+z[i][1]
        #     b=solve(i+1,temp)
        #     dp[i][temp]=max(a,b)
        #     return max(a,b)
        # z=list(zip(ages,scores))
        z=list(zip(scores,ages))
        z.sort()
        n=len(z)
        # dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        # return solve(0,-1)
        # bottom-up - TLE
        # dp=[[0 for i in range(n+1)] for j in range(n+1)]
        # ans=0
        # for i in range(n-1,-1,-1):
        #     flag=0
        #     for temp in range(n-1,-1,-1):
        #         a=0
        #         if(flag==0 or z[temp][1]<=z[i][1]):
        #             a=dp[i+1][i]+z[i][1]
        #             flag=1
        #         b=dp[i+1][temp]
        #         dp[i][temp]=max(a,b)
        #         ans=max(ans,dp[i][temp])
        # return ans
        
        #1-D dp
        dp = [0] * n
        for i in range(n):
            dp[i] = z[i][0]
        for i in range(n):
            for j in range(i):
                if z[i][1] >= z[j][1]:
                    dp[i] = max(dp[j] + z[i][0], dp[i])
        return max(dp)
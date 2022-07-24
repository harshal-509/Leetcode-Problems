class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(s,i,dp):
            if(i==n):
                return 1
            t=""
            if(dp[i]!=-1):
                return dp[i]
            for j in range(i,n):
                t+=s[j]
                if(z[t]):
                    if(solve(s,j+1,dp)):
                        dp[i]=1
                        return dp[i]
            dp[i]=0
            return dp[i]
        n=len(s)
        dp=[-1 for i in range(n+1)]
        z=Counter(wordDict)
        return solve(s,0,dp)
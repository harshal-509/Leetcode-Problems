class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        dp=[[0 for i in range(n+1)] for i in range(m+1)]
        dp[0][0]=1
        for i in range(1,m+1):
            if(p[i-1]=="*"):
                dp[i][0]=dp[i-1][0]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(s[j-1]==p[i-1] or p[i-1]=="?"):
                    dp[i][j]=dp[i-1][j-1]
                elif(p[i-1]=="*"):
                    dp[i][j]=dp[i-1][j]|dp[i][j-1]
        return dp[-1][-1]
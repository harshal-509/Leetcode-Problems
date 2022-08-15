class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(i,j):
            if(i>=n and j>=m):
                return 0
            if(i>=n):
                return m-j
            if(j>=m):
                return n-i
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(word1[i]!=word2[j]):
                a=solve(i,j+1)+1
                b=solve(i+1,j)+1
                c=solve(i+1,j+1)+1
                dp[i][j]=min(a,b,c)
                return min(a,b,c)
            else:
                a=solve(i+1,j+1)
                dp[i][j]=a
                return a
        n=len(word1)
        m=len(word2)
        dp=[[-1 for i in range(m)] for j in range(n)]
        return solve(0,0)
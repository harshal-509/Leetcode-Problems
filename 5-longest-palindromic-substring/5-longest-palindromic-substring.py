class Solution:
    @cache
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=s[0]
        ans1=1
        dp=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i]=1
        for i in range(1,n):
            if(s[i]==s[i-1]):
                dp[i-1][i]=1
                ans1=2
                ans=s[i-1:i+1]
        m=2
        for i in range(2,n):
            j=i-m
            k=i
            while(k<n):
                if(dp[j+1][k-1]==1 and s[j]==s[k]):
                    dp[j][k]=1
                    if(k-j+1>ans1):
                        ans1=k-j+1
                        ans=s[j:k+1]
                j+=1
                k+=1
            m+=1
        return ans
class Solution:
	def editDistance(self, s, t):
		# Code here
        n=len(s)
        m=len(t)
        dp=[[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for i in range(n+1):
            dp[0][i]=i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(t[i-1]==s[j-1]):
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[-1][-1]
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends
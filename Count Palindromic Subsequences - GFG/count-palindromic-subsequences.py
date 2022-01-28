class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPs(self,s):
        # Code here
        def hs(i,j,dp):
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(i>j):
                return 0
            if(i==j):
                dp[i][j]=1
                return 1
            if(s[i]==s[j]):
                dp[i][j]=1+hs(i+1,j,dp)+hs(i,j-1,dp)
                return dp[i][j]
            dp[i][j]=hs(i+1,j,dp)+hs(i,j-1,dp)-hs(i+1,j-1,dp)
            return dp[i][j]%mod
        n=len(s)
        i=0
        j=n-1
        mod=int(1e9+7)
        dp=[[-1 for i in range(n)] for j in range(n)]
        return hs(i,j,dp)

#{ 
#  Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPs(input().strip()))

# } Driver Code Ends
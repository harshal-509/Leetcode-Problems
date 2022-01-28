class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPs(self,s):
        # Code here
        n=len(s)
        mod=int(1e9+7)
        dp=[[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i]=1
        for i in range(1,n):
            if(s[i-1]==s[i]):
                dp[i-1][i]=1+dp[i-1][i-1]+dp[i][i]
            else:
                dp[i-1][i]=dp[i-1][i-1]+dp[i][i]
        for i in range(2,n):
            j=0
            k=i
            while(k<n):
                if(s[k]==s[j]):
                    dp[j][k]=1+dp[j+1][k]+dp[j][k-1]
                else:
                    dp[j][k]=dp[j+1][k]+dp[j][k-1]-dp[j+1][k-1]
                j+=1
                k+=1
        return dp[0][-1]%mod
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
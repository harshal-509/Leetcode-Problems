#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        dp=[[0 for i in range(x)] for j in range(y)]
        if(s1[0]==s2[0]):
            dp[0][0]=1
        for i in range(1,x):
            if(s1[i]==s2[0]):
                dp[0][i]=1
            else:
                dp[0][i]=dp[0][i-1]
        for i in range(1,y):
            if(s1[0]==s2[i]):
                dp[i][0]=1
            else:
                dp[i][0]=dp[i-1][0]
        for i in range(1,y):
            for j in range(1,x):
                if(s1[j]==s2[i]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
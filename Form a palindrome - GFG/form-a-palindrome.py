#User function Template for python3

class Solution:
    def countMin(self, s):
        # code here
        n=len(s)
        dp=[[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i]=1
        for i in range(1,n):
            j=0
            k=i
            while(k<n):
                if(s[j]==s[k]):
                    dp[j][k]=2+dp[j+1][k-1]
                else:
                    dp[j][k]=max(dp[j+1][k],dp[j][k-1])
                k+=1
                j+=1
        return n-dp[0][-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends
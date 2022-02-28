#User function Template for python3

class Solution:

    def findMinDiff(self, a,n,m):

        # code here
        a.sort()
        ans=a[-1]
        for i in range(n-m+1):
            ans=min(ans,a[i+m-1]-a[i])
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends
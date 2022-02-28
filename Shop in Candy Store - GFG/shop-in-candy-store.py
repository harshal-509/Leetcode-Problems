#User function Template for python3

class Solution:

    def candyStore(self, candies,n,k):
        # code here
        candies.sort()
        ans=0
        ans1=0
        i=0
        j=n-1
        while(i<=j):
            ans+=candies[i]
            i+=1
            j=j-k
        i=0
        j=n-1
        while(i<=j):
            ans1+=candies[j]
            j-=1
            i=i+k
        return ans,ans1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends
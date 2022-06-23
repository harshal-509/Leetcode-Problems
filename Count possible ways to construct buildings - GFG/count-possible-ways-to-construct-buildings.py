#User function Template for python3

class Solution:
	def TotalWays(self, N):
		# Code here
        a=2
        b=3
        if(N==1):
            c=a
        if(N==2):
            c=b
        t=2
        while(t<N):
            c=a+b
            a=b
            b=c
            t+=1
        return (c*c)%(int(1e9+7))
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends
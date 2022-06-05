#User function template for Python

class Solution:	
	def buzzTime(self, n, m, l, h, a):
		# code here
		def hs(mid):
		    t=0
		    for i in range(n):
		        x=h[i]+a[i]*(mid)
		        if(x>=l):
		            t+=x
		    return t>=m
        i=0
        j=max(m,l)
        ans=-1
        while(i<=j):
            mid=i+(j-i)//2
            if(hs(mid)):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M, L = [int(x) for x in input().split()]
        H = [0 for x in range(N)]
        A = [0 for x in range(N)]
        for i in range(N):
            H[i], A[i] = [int(y) for y in input().split()]
        ob = Solution()
        print(ob.buzzTime(N, M, L, H, A))

# } Driver Code Ends
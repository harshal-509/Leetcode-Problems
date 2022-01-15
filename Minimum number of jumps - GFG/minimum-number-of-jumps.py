#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if(arr[0]==0 and n!=1):
	        return -1
	    if(n==1):
	        return 0
	    s=arr[0]
	    l=arr[0]
	    i=1
	    ans=1
	    while(i<n-1):
	        if(i+arr[i]>l):
	            l=arr[i]+i
	        s-=1
	        if(s==0):
	            ans+=1
	            s=l-i
	            if(s==0):
	                return -1
	        i+=1
	    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
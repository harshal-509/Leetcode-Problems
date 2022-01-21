#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		ans=-100001
    	max_=1
    	min_=1
		for i in range(n):
		    max_=arr[i]*max_
	    	min_=arr[i]*min_
    		max_,min_=max(arr[i],max_,min_),min(arr[i],max_,min_)
    		ans=max(ans,max_)
	    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
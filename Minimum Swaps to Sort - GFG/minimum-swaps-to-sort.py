

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		arr=sorted(nums)
		h={}
		for i in range(n):
		    h[arr[i]]=i
		ans=0
		for i in range(n):
		    while(i!=h[nums[i]]):
		        nums[h[nums[i]]],nums[i]=nums[i],nums[h[nums[i]]]
		        ans+=1
		return ans
#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends
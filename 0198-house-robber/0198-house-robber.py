class Solution:
    def rob(self, nums: List[int]) -> int:
        l=0
        r=0
        n=len(nums)
        if(n==1):
            return nums[0]
        dp=[0 for i in range(n)]
        dp[0]=nums[0]
        dp[1]=nums[1]
        if(n==2):
            return max(dp)
        dp[2]=nums[0]+nums[2]
        for i in range(3,n):
            dp[i]=nums[i]+max(dp[i-2],dp[i-3])
        return max(dp[-1],dp[-2])
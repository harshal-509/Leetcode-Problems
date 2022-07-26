class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        def solve(nums,i):
            if(i>=n-1):
                return 0
            if(dp[i]!=-1):
                return dp[i]
            ans=float('inf')
            for j in range(i+1,i+1+nums[i]):
                ans=min(ans,solve(nums,j)+1)
            dp[i]=ans
            return dp[i]
        dp=[-1 for i in range(n+1)]
        return solve(nums,0)
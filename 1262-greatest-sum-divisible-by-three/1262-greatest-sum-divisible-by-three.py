class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def solve(i,m):
            if(i>=n):
                if(m==0):
                    return 0
                return -float('inf')
            a=solve(i+1,(nums[i]+m)%3)+nums[i]
            b=solve(i+1,m)
            return max(a,b)
        n=len(nums)
        return solve(0,0)
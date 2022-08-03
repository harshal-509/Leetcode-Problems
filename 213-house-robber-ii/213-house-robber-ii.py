class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums,i,j):
            if(i==j-1):
                return nums[i]
            if(i==j-2):
                return max(nums[i],nums[i+1])
            if(i==j-3):
                return max(nums[i+1],nums[i]+nums[i+2])
            first=nums[i]
            second=nums[i+1]
            third=nums[i+2]+first
            for k in range(i+3,j):
                curr=max(first,second)+nums[k]
                first=second
                second=third
                third=curr
            return max(third,second)
        n=len(nums)
        if(n==1):
            return nums[0]
        if(n==2):
            return max(nums[0],nums[1])
        if(n==3):
            return max(nums[0],nums[1],nums[2])
        return max(solve(nums,0,n-1),solve(nums,1,n))
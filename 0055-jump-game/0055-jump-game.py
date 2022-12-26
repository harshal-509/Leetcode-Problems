class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ma=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]+i>=ma):
                ma=i
        return ma==0
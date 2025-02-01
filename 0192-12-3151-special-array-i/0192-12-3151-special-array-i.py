class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return bool(1)
        for i in range(1,len(nums)):
            if(nums[i]%2 == nums[i-1]%2):
                return bool(0)
        return bool(1)
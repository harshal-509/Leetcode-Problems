class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        flag=0
        for i in range(n-1):
            if(nums[i]>nums[i+1]):
                flag+=1
        if(nums[-1]>nums[0]):
            flag+=1
        return flag<=1
                
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def check(x):
            t=0
            for i in range(len(nums)):
                if(nums[i]>=x):
                    t+=1
            return t==x
        nums.sort()
        i=0
        j=nums[-1]
        for k in range(i,j+1):
            if(check(k)):
                return k
        return -1

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans=0
        z=Counter([0,nums[0]])
        a=nums[0]
        if(nums[0]==0):
            ans+=1
        for i in range(1,len(nums)):
            a^=nums[i]
            if(z[a]):
                ans+=z[a]
            z[a]+=1
        return ans
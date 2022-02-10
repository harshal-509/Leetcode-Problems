class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        for i in range(1,n):
            nums[i]=nums[i]+nums[i-1]
        z=Counter([0])
        ans=0
        for i in nums:
            ans+=z[i-k]
            z[i]=z[i]+1
        return ans
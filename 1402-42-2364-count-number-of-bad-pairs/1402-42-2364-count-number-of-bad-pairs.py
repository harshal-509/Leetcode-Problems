class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]-=i
        z=Counter(nums)
        ans=0
        for i in nums:
            ans+=n-z[i]
        return ans//2
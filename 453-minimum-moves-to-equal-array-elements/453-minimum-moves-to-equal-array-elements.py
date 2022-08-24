class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        nums.sort()
        for i in range(n-1):
            ans+=(nums[i+1]-nums[i])*(n-1-i)
        return ans
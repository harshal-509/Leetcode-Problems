class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=len(nums)
        return (k*(k+1))//2-sum(nums)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z=Counter(nums)
        for x in z:
            if(z[x]==1):
                return x
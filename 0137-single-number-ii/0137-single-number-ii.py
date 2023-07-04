class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z=Counter(nums)
        for i in z:
            if(z[i]==1):
                return i
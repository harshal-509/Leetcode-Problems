class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        d = [defaultdict(int) for _ in range(len(nums))]
        ans=0
        for i in range(1,len(nums)):
            for j in range(i):
                cd = nums[i]-nums[j]
                jj = d[j][cd]
                ii = d[i][cd]
                ans+=jj
                d[i][cd]=jj+ii+1
        return ans
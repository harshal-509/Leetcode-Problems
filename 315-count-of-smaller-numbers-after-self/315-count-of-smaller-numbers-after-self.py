class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        a=[]
        n=len(nums)
        ans=[-1 for i in range(n)]
        for i in range(n-1,-1,-1):
            x=bisect_left(a,nums[i])
            insort(a,nums[i])
            ans[i]=x
        return ans
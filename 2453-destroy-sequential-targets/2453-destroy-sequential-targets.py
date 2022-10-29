class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        n=len(nums)
        t=[0 for i in range(n)]
        for i in range(len(nums)):
            t[i]=nums[i]%space
        z=Counter(t)
        t1=0
        for i in z:
            t1=max(z[i],t1)
        ans=float('inf')
        for i in range(n):
            if(z[t[i]]==t1):
                ans=min(ans,nums[i])
        return ans
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans=min(divisors)
        n=len(nums)
        m=len(divisors)
        s=0
        for i in range(m):
            t=0
            for j in range(n):
                if(nums[j]%divisors[i]==0):
                    t+=1
            if(t>s):
                s=t
                ans=divisors[i]
            if(t==s):
                ans=min(ans,divisors[i])
        return ans
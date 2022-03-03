class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==0 or n==1 or n==2):
            return 0
        ans=0
        t=0
        for i in range(1,n-1):
            if(nums[i+1]-nums[i]==nums[i]-nums[i-1]):
                if(t==0):
                    t=3
                else:
                    t+=1
            else:
                if(t):
                    ans+=(t*(t+1)//2)-(t)-(t-1)
                t=0
        if(t):
            ans+=(t*(t+1)//2)-(t)-(t-1)
        return ans
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return 0
        suf=[0 for i in range(n)]
        pre=[0 for i in range(n)]
        suf[-1]=nums[-1]
        pre[0]=nums[0]
        for i in range(n-2,-1,-1):
            suf[i]=suf[i+1]+nums[i]
        ans=0
        ans1=abs(pre[0]-suf[1]//(n-1))
        for i in range(1,n):
            pre[i]=pre[i-1]+nums[i]
        for i in range(1,n-1):
            t=abs(pre[i]//(i+1)-suf[i+1]//(n-i-1))
            if(t<ans1):
                ans1=t
                ans=i
        t=abs(pre[-1]//(n))
        if(t<ans1):
            ans1=t
            ans=n-1
        return ans
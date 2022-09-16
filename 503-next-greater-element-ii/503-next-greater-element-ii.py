class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        m=max(nums)
        t=0
        ans=[0 for i in range(n)]
        for i in range(n):
            if(nums[i]==m):
                ans[i]=-1
                t=i
        s=[]
        p=t
        while(t>=0):
            if(s):
                while(s and s[-1]<=nums[t]):
                    s.pop()
                if(s):
                    ans[t]=s[-1]
                else:
                    ans[t]=-1
                s.append(nums[t])
            else:
                ans[t]=-1
                s.append(nums[t])           
            t-=1
        t=n-1
        while(t>p):
            if(s):
                while(s and s[-1]<=nums[t]):
                    s.pop()
                if(s):
                    ans[t]=s[-1]
                else:
                    ans[t]=-1
                s.append(nums[t])
            else:
                ans[t]=-1
                s.append(nums[t])            
            t-=1
        return ans
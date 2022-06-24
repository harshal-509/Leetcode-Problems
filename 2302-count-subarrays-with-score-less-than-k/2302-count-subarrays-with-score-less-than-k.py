class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        i=0
        j=0
        n=len(nums)
        t=0
        c=1
        while(i<n and j<n):
            if(nums[i]>=k):
                i=j
            if((t+nums[j])*c<k):
                t+=nums[j]
                c+=1
            else:
                p=(j-i)
                ans+=(p*(p+1))//2
                while(i<j and (t+nums[j])*c>=k):
                    t-=nums[i]
                    c-=1
                    i+=1
                p=(j-i)
                ans-=(p*(p+1))//2
                c+=1
                t+=nums[j]
            j+=1
        if(nums[i]>=k):
            i=j
        p=(j-i)
        ans+=(p*(p+1))//2
        return ans
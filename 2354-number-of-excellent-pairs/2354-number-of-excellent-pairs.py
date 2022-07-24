class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums=list(set(nums))
        n=len(nums)
        for i in range(n):
            nums[i]=bin(nums[i]).count('1')
        nums.sort()
        ans=0
        for i in range(n):
            if(nums[i]>=k):
                ans+=(n-i)*2-1
            else:
                x=bisect_left(nums,k-nums[i],i,n)
                if(x==i):
                    ans-=1
                ans+=2*(n-x)
        return ans
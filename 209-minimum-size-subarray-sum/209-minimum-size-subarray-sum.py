class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        ans=float('inf')
        temp=0
        n=len(nums)
        while(i<n and j<n):
            if(temp>=target):
                while(i<j and temp>=target):
                    ans=min(ans,j-i)
                    temp-=nums[i]
                    i+=1
            else:
                temp+=nums[j]
                j+=1
        if(temp>=target):
            while(i<j and temp>=target):
                ans=min(ans,j-i)
                temp-=nums[i]
                i+=1
        if(ans==float('inf')):
            return 0
        return ans
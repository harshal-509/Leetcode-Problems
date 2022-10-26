class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        nums1=[nums[i] for i in range(n)]
        for i in range(1,n):
            nums1[i]+=nums1[i-1]
        for i in range(n):
            nums1[i]%=k
        z=Counter([])
        z[0]=0
        for i in range(n):
            if(z[nums1[i]] and i-(z[nums1[i]]-1)>=2):
                return 1
            if(nums1[i]!=0):
                if(z[nums1[i]]):
                    z[nums1[i]]=min(z[nums1[i]],i+1)
                else:
                    z[nums1[i]]=i+1
            else:
                if(i-(z[nums1[i]]-1)>=2):
                    return 1
        return 0
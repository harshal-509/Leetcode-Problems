class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        while(i<=j):
            m=i+(j-i)//2
            if(nums[m]==target):
                return m
            if(nums[i]<=nums[m]):
                if(nums[m]>target and target>=nums[i]):
                    j=m-1
                else:
                    i=m+1
            else:
                if(target>=nums[m] and target<=nums[j]):
                    i=m+1
                else:
                    j=m-1
        return -1

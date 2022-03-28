class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            midNum=nums[mid]
            if midNum==target:
                return True
            if midNum>nums[l]:
                if target<nums[l] or midNum<target:
                    l=mid+1
                else:
                    r=mid-1
            elif midNum<nums[l]:
                if target>nums[r] or midNum>target:
                    r=mid-1
                else:
                    l=mid+1
            else:
                l+=1
        return False
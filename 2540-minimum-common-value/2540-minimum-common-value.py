class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        while(i<n and j<m):
            if(nums1[i]==nums2[j]):
                return nums1[i]
            if(nums1[i]<nums2[j]):
                i+=1
            else:
                j+=1
        return -1
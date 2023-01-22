class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a=0
        b=0
        if(k==0):
            if(nums1==nums2):
                return 0
            return -1
        n=len(nums1)
        for i in range(n):
            x=nums1[i]-nums2[i]
            if(x%k):
                return -1
            if(x>=0):
                a+=x
            else:
                b+=abs(x)
        if(a==b):
            return a//k
        return -1
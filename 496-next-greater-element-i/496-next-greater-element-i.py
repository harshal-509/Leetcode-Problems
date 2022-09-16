class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        n=len(nums1)
        m=len(nums2)
        z=Counter([])
        for i in range(m-1,-1,-1):
            if(s):
                while(s and s[-1]<=nums2[i]):
                    s.pop()
                if(s):
                    z[nums2[i]]=s[-1]
                else:
                    z[nums2[i]]=-1
                s.append(nums2[i])
            else:
                z[nums2[i]]=-1
                s.append(nums2[i])
        sol=[]
        for i in range(n):
            sol.append(z[nums1[i]])
        return sol
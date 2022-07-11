class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        z=Counter([])
        k=k1+k2
        n=len(nums1)
        for i in range(n):
            x=abs(nums1[i]-nums2[i])
            z[x]+=1
        t=sorted(z,reverse=True)
        for i in range(t[0],0,-1):
            while(z[i] and k):
                if(k>=z[i]):
                    z[i-1]+=z[i]
                    k-=z[i]
                    z[i]=0
                else:
                    z[i]-=k
                    z[i-1]+=k
                    k=0
        ans=0
        for i in range(t[0],0,-1):
            ans+=z[i]*(i*i)
        return ans
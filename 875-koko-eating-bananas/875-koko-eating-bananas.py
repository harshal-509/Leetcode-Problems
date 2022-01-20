import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hs(m):
            a=0
            for i in piles:
                a+=math.ceil(i/m)
            return a<=h    
        i=1
        j=max(piles)
        ans=-1
        while(i<=j):
            m=i+(j-i)//2
            if(hs(m)):
                ans=m
                j=m-1
            else:
                i=m+1
        return ans
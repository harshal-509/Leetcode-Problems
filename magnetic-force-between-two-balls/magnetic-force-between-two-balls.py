class Solution:
    def maxDistance(self, position: List[int], k: int) -> int:
        def hs(l,r,m):
            c=1
            p=position[0]
            for i in range(n):
                if(position[i]-p>=m):
                    c+=1
                    if(c==k):
                        return 1
                    p=position[i]
            return 0
        l=0
        r=0
        n=len(position)
        for i in range(n):
            r=max(r,position[i])
        ans=0
        position.sort()
        while(l<=r):
            m=l+(r-l)//2
            if(hs(l,r,m)):
                l=m+1
                ans=m
            else:
                r=m-1
        return ans

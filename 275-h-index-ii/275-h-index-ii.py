class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def hs(mid):
            a=0
            for i in range(n):
                if(citations[i]>=mid):
                    a+=1
            if(a>=mid):
                return 1
            return 0
        ans=-1
        i=0
        j=len(citations)
        n=j
        while(i<=j):
            mid=i+(j-i)//2
            if(hs(mid)):
                ans=mid
                i=mid+1
            else:
                j=mid-1
        return ans
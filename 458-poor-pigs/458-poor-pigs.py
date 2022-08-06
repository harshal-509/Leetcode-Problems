class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        def solve(m):
            if(t**m>=buckets):
                return 1
            return 0
        i=0
        j=buckets
        t=minutesToTest//minutesToDie+1
        ans=-1
        while(i<=j):
            mid=i+(j-i)//2
            x=solve(mid)
            if(x):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
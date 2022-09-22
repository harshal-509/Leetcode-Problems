class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        i=1
        n=len(dist)
        j=10000000
        ans=-1
        while(i<=j):
            mid=i+(j-i)//2
            t=0
            flag=0
            for k in range(n-1):
                t+=int(math.ceil(dist[k]/mid))
                if(t>hour):
                    flag=1
                    break
            if(flag==0 and t+dist[-1]/mid<=hour):
                ans=mid
                j=mid-1
            else:
                i=mid+1
        return ans
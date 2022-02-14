class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(startTime)
        z=list(zip(startTime,endTime,profit))
        z=sorted(z,key=lambda x:x[1])
        dp=[0 for i in range(n)]
        dp[0]=z[0][2]
        for k in range(1,n):
            i=0
            j=k-1
            ans=-1
            while(i<=j):
                m=i+(j-i)//2
                if(z[m][1]<=z[k][0]):
                    ans=m
                    i=m+1
                else:
                    j=m-1
            if(ans!=-1):
                dp[k]=max(dp[ans]+z[k][2],dp[k-1])
            else:
                dp[k]=max(z[k][2],dp[k-1])
        return dp[-1]
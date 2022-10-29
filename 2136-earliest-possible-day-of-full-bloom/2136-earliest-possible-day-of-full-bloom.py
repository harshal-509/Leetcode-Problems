class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        z=list(zip(plantTime,growTime))
        z.sort(key=lambda x:x[0],reverse=True)
        z.sort(key=lambda x:x[1],reverse=True)
        ans=0
        n=len(plantTime)
        t=0
        for i in range(n):
            t+=z[i][0]
            ans=max(ans,t+z[i][1])
        return ans
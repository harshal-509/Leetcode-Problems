class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans=0
        x=startValue
        y=target
        while(x<y):
            if(y%2==0):
                y=y//2
                ans+=1
            else:
                y+=1
                ans+=1
        return ans+x-y
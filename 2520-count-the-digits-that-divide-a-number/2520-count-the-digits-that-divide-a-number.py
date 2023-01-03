class Solution:
    def countDigits(self, num: int) -> int:
        t=list(map(int,str(num)))
        ans=0
        for i in range(len(t)):
            if(num%t[i]==0):
                ans+=1
        return ans
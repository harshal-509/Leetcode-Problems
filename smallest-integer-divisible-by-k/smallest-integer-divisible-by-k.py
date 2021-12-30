class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        x=1
        ans=1
        for i in range(k):
            if(x%k==0):
                return ans
            ans+=1
            x=x*10+1
        return -1
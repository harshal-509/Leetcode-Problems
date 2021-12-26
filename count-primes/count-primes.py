class Solution:
    def countPrimes(self, n: int) -> int:
        ans=0
        p=[1 for i in range(n)]
        for i in range(2,n):
            if(p[i]):
                ans+=1
                for j in range(2*i,n,i):
                    p[j]=0
        return ans
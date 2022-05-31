class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        h=Counter([])
        n=len(s)
        for i in range(n-k+1):
            a=""
            for j in range(i,k+i):
                a+=s[j]
            h[a]+=1
        return len(h)==pow(2,k)
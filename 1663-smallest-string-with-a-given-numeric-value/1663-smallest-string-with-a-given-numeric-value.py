class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        a=['a' for i in range(n)]
        k-=n
        for i in range(n-1,-1,-1):
            if(k>=25):
                k-=25
                a[i]='z'
            else:
                a[i]=chr(97+k)
                break
        return "".join(a)
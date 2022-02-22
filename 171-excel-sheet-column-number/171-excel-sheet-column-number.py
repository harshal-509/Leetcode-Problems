class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        h={}
        for i in range(65,91):
            h[chr(i)]=abs(64-i)
        ans=0
        n=len(columnTitle)
        for i in range(n):
            ans+=h[columnTitle[i]]*pow(26,n-i-1)
        return ans
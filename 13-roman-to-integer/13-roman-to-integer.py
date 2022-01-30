class Solution:
    def romanToInt(self, s: str) -> int:
        h={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=h[s[0]]
        n=len(s)
        for i in range(1,n):
            if(h[s[i-1]]>=h[s[i]]):
                ans+=h[s[i]]
            else:
                ans+=h[s[i]]-2*h[s[i-1]]
        return ans
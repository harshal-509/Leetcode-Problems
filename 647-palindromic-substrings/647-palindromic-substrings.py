class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            a=""
            b=""
            for j in range(i,n):
                a+=s[j]
                b=s[j]+b
                if(a==b):
                    ans+=1
        return ans
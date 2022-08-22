class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        t=""
        p=""
        x="0"
        y="1"
        for i in range(n):
            t+=x
            p+=y
            x,y=y,x
        ans=0
        ans1=0
        for i in range(n):
            if(s[i]!=t[i]):
                ans+=1
            if(s[i]!=p[i]):
                ans1+=1
        return min(ans,ans1)
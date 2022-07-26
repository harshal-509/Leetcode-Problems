class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(i,j,s,p):
            if(j==-1 and i>=0):
                return 0
            if(i==-1):
                if(i==j):
                    return 1
                if(j>=0 and p[j]!="*"):
                    return 0
            ans=0
            if(i>=0 and s[i]==p[j]):
                ans=solve(i-1,j-1,s,p)
            if(j>=0 and p[j]=="."):
                ans=solve(i-1,j-1,s,p)
            if(j>=0 and p[j]=="*"):
                x=p[j-1]
                if(x=="."):
                    ans=0
                    while(i>=0):
                        ans|=solve(i,j-2,s,p)
                        i-=1
                    ans|=solve(i,j-2,s,p)
                else:
                    ans=0
                    while(i>=0 and x==s[i]):
                        ans|=solve(i,j-2,s,p)
                        i-=1
                    ans|=solve(i,j-2,s,p)
            return ans
        n=len(s)
        m=len(p)
        return solve(n-1,m-1,s,p)
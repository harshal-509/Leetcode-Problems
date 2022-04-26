class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def solve(s,x):
            if(z[s]):
                return
            z[s]+=1
            if(x==0):
                if(minremoval(s)==0):
                    ans.append(s)
                return
            if(x<0):
                return
            for i in range(len(s)):
                solve(s[:i]+s[i+1:],x-1)
        def minremoval(s):
            p=[]
            n=len(s)
            for i in range(n):
                if(s[i]==")"):
                    if(p and p[-1]=="("):
                        p.pop()
                    else:
                        p.append(s[i])
                elif(s[i]=="("):
                    p.append(s[i])
            return len(p)
        ans=[]
        z=Counter([])
        x=minremoval(s)
        solve(s,x)
        return ans
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans=[]
        n=len(s)
        m=float('inf')
        for i in range(n):
            a=0
            p=""
            for j in range(i,n):
                if(s[j]=="1"):
                    a+=1
                p+=s[j]
                if(a==k):
                    ans.append(p)
                    m=min(m,len(p))
                    break
        if(ans):
            t=[]
            for i in ans:
                if(len(i)==m):
                    t.append(i)
            t.sort()
            return t[0]
        return ""
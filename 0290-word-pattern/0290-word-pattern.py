class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n=len(pattern)
        a=[[] for i in range(26)]
        s=s.split()
        m=len(s)
        if(n!=m):
            return 0
        for i in range(n):
            a[ord(pattern[i])-97].append(i)
        h={}
        for i in range(26):
            t=len(a[i])
            if(t>=1):
                x=s[a[i][0]]
                for k in h:
                    if(h[k]==x):
                        return 0
                for j in a[i]:
                    if(x!=s[j]):
                        return 0
                h[chr(i+97)]=x
        return 1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if(m<n):
            return 0
        h=[0 for i in range(26)]
        i=0
        while(i<n):
            h[ord(s1[i])-97]+=1
            i+=1
        p=[0 for i in range(26)]
        i=0
        while(i<n):
            p[ord(s2[i])-97]+=1
            i+=1
        j=0
        while(i<m):
            a=0
            for k in range(26):
                if(h[k]==p[k]):
                    a+=1
            if(a==26):
                return 1
            p[ord(s2[j])-97]-=1
            p[ord(s2[i])-97]+=1
            i+=1
            j+=1
        a=0
        for k in range(26):
            if(h[k]==p[k]):
                a+=1
        if(a==26):
            return 1
        return 0
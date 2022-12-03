class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        n=len(s)
        m=len(t)
        a=0
        while(i<n and j<m):
            if(s[i]==t[j]):
                i+=1
                j+=1
                a+=1
            else:
                i+=1
        return m-a
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        n=len(s1)
        for i in range(n):
            if(s1[i]!=s2[i]):
                if(c==0):
                    t=s1[i]
                    p=s2[i]
                elif(c==1):
                    if(t==s2[i] and p==s1[i]):
                        pass
                    else:
                        return False
                c+=1
        return c==0 or c==2
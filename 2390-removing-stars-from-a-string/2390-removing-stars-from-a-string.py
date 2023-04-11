class Solution:
    def removeStars(self, s: str) -> str:
        ans=""
        n=len(s)
        i=n-1
        c=0
        while(i>=0):
            if(s[i]=="*"):
                c+=1
            else:
                if(c):
                    c-=1
                    pass
                else:
                    ans+=s[i]
            i-=1
        return ans[::-1]
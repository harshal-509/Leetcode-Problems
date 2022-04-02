class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pal(s):
            return s==s[::-1]
        flag=0
        i=0
        n=len(s)
        j=n-1
        while(i<j):
            if(s[i]!=s[j]):
                return pal(s[:i]+s[i+1:]) or pal(s[:j]+s[j+1:])
            else:
                i+=1
                j-=1
        return 1
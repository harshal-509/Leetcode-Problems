class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        i=0
        j=len(s)-1
        for i in range(97,123):
            k=chr(i)
            first=-1
            for j in range(len(s)):
                if(s[j]==k):
                    first=j
                    break
            last=-1
            for j in range(len(s)-1,-1,-1):
                if(s[j]==k):
                    last=j
                    break
            if(first==last or first==-1):
                pass
            else:
                ans+=len(set(s[first+1:last]))
        return ans
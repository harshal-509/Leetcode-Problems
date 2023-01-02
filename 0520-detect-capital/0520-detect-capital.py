class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n=len(word)
        t=0
        for i in word:
            if(ord(i)>=65 and ord(i)<=91):
                t+=1
        if(t==n or t==0 or (t==1 and ord(word[0])>=65 and ord(word[0])<=91)):
            return 1
        return 0
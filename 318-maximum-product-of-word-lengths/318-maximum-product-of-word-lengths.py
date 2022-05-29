class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        ans=0
        for i in range(n):
            a=0
            for j in range(len(words[i])):
                a|=(1<<ord(words[i][j])-97)
            words[i]=(words[i],a)
        for i in range(n):
            for j in range(n):
                if(words[i][1] & words[j][1]==0):
                    ans=max(ans,len(words[i][0])*len(words[j][0]))
        return ans
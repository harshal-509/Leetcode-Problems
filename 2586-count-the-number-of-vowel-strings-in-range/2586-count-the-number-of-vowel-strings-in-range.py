class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans=0
        def isvowel(t):
            if(t in ['a','e','i','o','u']):
                return 1
            return 0
        for i in range(left,right+1):
            if(isvowel(words[i][0]) and isvowel(words[i][-1])):
                ans+=1
        return ans
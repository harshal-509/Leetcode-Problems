class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def solve(s,i):
            if(i==n):
                return 1
            t=""
            for j in range(i,n):
                t+=s[j]
                if(z[t]):
                    if(solve(s,j+1)):
                        return 1
            return 0
        n=len(s)
        z=Counter(wordDict)
        return solve(s,0)
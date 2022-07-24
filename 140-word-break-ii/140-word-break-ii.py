class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def solve(s,i,temp):
            if(i==n):
                p=" ".join(temp)
                ans.append(p)
                return 1
            t=""
            for j in range(i,n):
                t+=s[j]
                if(z[t]):
                    temp.append(t)
                    solve(s,j+1,temp)
                    temp.pop()
        n=len(s)
        ans=[]
        dp=[-1 for i in range(n+1)]
        z=Counter(wordDict)
        solve(s,0,[])
        return ans
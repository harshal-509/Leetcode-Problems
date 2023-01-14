class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def dfs(i):
            if(i not in s):
                s.add(i)
                ans=i
                for j in d[i]:
                    ans=min(ans,dfs(j))
                return ans
            return i
        d=defaultdict(list)
        n=len(s1)
        for i in range(n):
            d[s1[i]].append(s2[i])
            d[s2[i]].append(s1[i])
        for i in d:
            d[i].sort()
        ans=""
        for i in baseStr:
            if(d[i]):
                s=set()
                x=dfs(d[i][0])
                ans+=min(i,x)
            else:
                ans+=i
        return ans
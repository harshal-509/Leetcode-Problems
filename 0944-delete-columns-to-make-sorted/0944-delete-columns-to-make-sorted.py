class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])
        ans=0
        for i in range(m):
            t=""
            for j in range(n):
                t+=strs[j][i]
            if(sorted(t)!=list(t)):
                ans+=1
        return ans
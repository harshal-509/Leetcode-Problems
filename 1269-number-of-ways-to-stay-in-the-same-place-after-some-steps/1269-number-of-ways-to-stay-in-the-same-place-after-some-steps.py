class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def solve(i,n,s):
            if(s==steps and i==0):
                return 1
            if(i<0 or i>=n or s>=steps):
                return 0
            a=0
            a+=solve(i+1,n,s+1)
            a+=solve(i,n,s+1)
            a+=solve(i-1,n,s+1)
            return a
        return solve(0,arrLen,0)%(int(1e9+7))
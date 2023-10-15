class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def solve(curr,remsteps):
            if(curr<0 or curr>=arrLen or remsteps<0):
                return 0
            if(curr==0 and remsteps==0):
                return 1
            return solve(curr+1,remsteps-1)+solve(curr-1,remsteps-1)+solve(curr,remsteps-1)
        return solve(0,steps)%int(1e9+7)
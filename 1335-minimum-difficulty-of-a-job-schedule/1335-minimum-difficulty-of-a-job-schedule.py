class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def solve(i,k,temp):
            if(i>=n):
                if(k==d):
                    return temp
                return float('inf')
            a=solve(i+1,k,max(jobDifficulty[i],temp))
            b=solve(i+1,k+1,jobDifficulty[i])+temp
            return min(a,b)
        n=len(jobDifficulty)
        if(d>n):
            return -1
        return solve(0,0,0)
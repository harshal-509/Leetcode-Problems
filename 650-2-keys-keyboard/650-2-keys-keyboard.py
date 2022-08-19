class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def solve(i,t,c):
            if(i==n):
                return 0
            if(t==n):
                return 0
            a=float('inf')
            b=float('inf')
            if(i+t<=n):
                a=solve(i+t,t,0)+1
            if(c==0):
                b=solve(i,i,1)+1
            return min(a,b)
        if(n==1):
            return 0
        return solve(1,1,0)+1
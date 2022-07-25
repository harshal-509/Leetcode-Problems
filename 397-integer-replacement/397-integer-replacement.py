class Solution:
    def integerReplacement(self, n: int) -> int:
        def solve(n,s):
            if(n==1):
                return s
            if(n%2):
                x=solve(n+1,s+1)
                y=solve(n-1,s+1)
                return min(x,y)
            else:
                return solve(n//2,s+1)
        return solve(n,0)
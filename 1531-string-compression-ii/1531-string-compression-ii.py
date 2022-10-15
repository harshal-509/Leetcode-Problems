class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def solve(k,i,j,c):
            if(k<0):
                return float('inf')
            if(i>=n):
                return 0
            if(0<=j<n and s[i]==s[j]):
                a=solve(k,i+1,i,c+1)
                b=float('inf')
                return min(b,int(c == 1 or c == 9 or c==99)+a)
            else:
                a=solve(k,i+1,i,1)
                b=solve(k-1,i+1,j,c)
                return min(1+a,b)
        n=len(s)
        return solve(k,0,-1,0)
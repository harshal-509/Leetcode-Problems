class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if(i>=n):
                return 0
            if(j>=n or j<0):
                return float('inf')
            b=solve(i+1,j)
            c=solve(i+1,j-1)
            d=solve(i+1,j+1)
            return min(b,c,d)+matrix[i][j]
        n=len(matrix)
        ans=float('inf')
        for i in range(n):
            ans=min(ans,solve(0,i))
        return ans
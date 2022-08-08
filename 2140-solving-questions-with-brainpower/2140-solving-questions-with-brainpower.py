class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def solve(i):
            if(i>=n):
                return 0
            if(dp[i]!=-1):
                return dp[i]
            a=solve(i+1)
            b=solve(i+questions[i][1]+1)+questions[i][0]
            dp[i]=max(a,b)
            return max(a,b)
        n=len(questions)
        dp=[-1 for i in range(n+1)]
        return solve(0)
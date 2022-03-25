class Solution:
    def __init__(self):
        self.ans=float('inf')
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def solve(l,i,a,b):
            if(a>n or b>n or i>=2*n):
                return 0
            if(a==n):
                return l[i][1]+solve(l,i+1,a,b+1)
            if(b==n):
                return l[i][0]+solve(l,i+1,a+1,b)
            if(dp[a][b]!=-1):
                return dp[a][b]
            x=l[i][0]+solve(l,i+1,a+1,b)
            y=l[i][1]+solve(l,i+1,a,b+1)
            dp[a][b]=min(x,y)
            return dp[a][b]
        a=0
        b=0
        n=len(costs)//2
        dp=[[-1 for i in range(n+1)] for i in range(n)]
        return solve(costs,0,a,b)
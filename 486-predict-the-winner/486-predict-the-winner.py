class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def solve(i,j,x,a,b):
            if(i>j):
                if(a>=b):
                    return 1
                return 2
            if(dp[i][j][x][(a,b)]):
                return dp[i][j][x][(a,b)]
            if(x==1):
                p=solve(i+1,j,x^1,a+nums[i],b)
                q=solve(i,j-1,x^1,a+nums[j],b)
                if(p==1 or q==1):
                    dp[i][j][x][(a,b)]=1
                    return 1
                dp[i][j][x][(a,b)]=2
                return 2
            else:
                p=solve(i+1,j,x^1,a,b+nums[i])
                q=solve(i,j-1,x^1,a,b+nums[j])
                if(p==1 and q==1):
                    dp[i][j][x][(a,b)]=1
                    return 1
                dp[i][j][x][(a,b)]=2
                return 2
        n=len(nums)
        dp=[[[Counter([]) for j in range(2)] for i in range(n+1)] for k in range(n+1)]
        return solve(0,n-1,1,0,0)==1
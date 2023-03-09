class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # bottom-up TLE don't know why
        # @cache
        # def solve(i,tar,count):
        #     if(i>=n or tar>target):
        #         return 0
        #     if(tar==target):
        #         return 1
        #     a=0
        #     if(count<types[i][0]):
        #         a+=solve(i,tar+types[i][1],count+1)
        #     a+=solve(i+1,tar,0)
        #     return a
        # n=len(types)
        # return solve(0,0,0)%int(1e9+7)
    
        #Top-Down
        # n=len(types)
        # dp=[[[0 for i in range(51)] for j in range(target+1)] for k in range(n+1)]
        # for i in range(n+1):
        #     for j in range(51):
        #         dp[i][target][j]=1
        # for i in range(n-1,-1,-1):
        #     for j in range(target,-1,-1):
        #         for k in range(types[i][0],-1,-1):
        #             a=0
        #             if(k<types[i][0] and j+types[i][1]<=target):
        #                 a+=dp[i][j+types[i][1]][k+1]
        #             a+=dp[i+1][j][0]
        #             dp[i][j][k]=a
        # return dp[0][0][0]%int(1e9+7)
        
        @cache
        def dfs(i, target):
            if target == 0: return 1
            if i >= len(types) or target < 0: return 0
            return sum(dfs(i + 1, target - j * types[i][1]) for j in range(types[i][0] + 1)) % 1000000007
        return dfs(0, target)
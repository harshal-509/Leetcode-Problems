class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

#         TLE - Top down
#         @cache
#         def solve(i,k):
#             if(k==m):
#                 return 0
#             if((i,k) in dp):
#                 return dp[(i,k)]
            
#             a=solve(i+1,k+1)+nums[i]*multipliers[k]
#             b=solve(i,k+1)+nums[(n-1)-(k-i)]*multipliers[k]
#             dp[(i,k)]=max(a,b)
#             return max(a,b)
#         n=len(nums)
#         m=len(multipliers)
#         dp={}
#         return solve(0,0)
        
    
    
    #using lru_cache(2000) instead of cache
#         lru_cache(2000)
#         def solve(i,k):
#             if(k==m):
#                 return 0
#             if((i,k) in dp):
#                 return dp[(i,k)]
            
#             a=solve(i+1,k+1)+nums[i]*multipliers[k]
#             b=solve(i,k+1)+nums[(n-1)-(k-i)]*multipliers[k]
#             dp[(i,k)]=max(a,b)
#             return max(a,b)
#         n=len(nums)
#         m=len(multipliers)
#         dp={}
#         return solve(0,0)




#         TLE - bottom up
#         n=len(nums)
#         m=len(multipliers)
#         dp=[[0 for i in range(m+1)] for j in range(m+1)]
#         for k in range(m-1,-1,-1):
#             for i in range(k,-1,-1):
#                 a=dp[i+1][k+1]+nums[i]*multipliers[k]
#                 b=dp[i][k+1]+nums[(n-1)-(k-i)]*multipliers[k]
#                 dp[i][k]=max(a,b)
#         return dp[0][0]





        n=len(nums)
        m=len(multipliers)
        prev = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            cur = [0] * (i + 2)
            for left in range(i, -1, -1):
                right = n + left - i - 1
                cur[left] = max(nums[left] * multipliers[i] + prev[left + 1],
                                nums[right] * multipliers[i] + prev[left])
            prev = cur

        return prev[0]
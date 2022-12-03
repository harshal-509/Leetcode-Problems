class Solution:
    def countPalindromes(self, s: str) -> int:
#         @cache
#         def solve(c,i,first,second):
#             if(c==5):
#                 return 1
#             if(i>=n):
#                 return 0
#             if(c==0):
#                 a=solve(c+1,i+1,s[i],second)
#                 b=solve(c,i+1,first,second)
#             elif(c==1):
#                 a=solve(c+1,i+1,first,s[i])
#                 b=solve(c,i+1,first,second)
#             elif(c==2):
#                 a=solve(c+1,i+1,first,second)
#                 b=solve(c,i+1,first,second)
#             elif(c==3):
#                 a=0
#                 if(s[i]==second):
#                     a=solve(c+1,i+1,first,s[i])
#                 b=solve(c,i+1,first,second)
#             elif(c==4):
#                 a=0
#                 if(s[i]==first):
#                     a=solve(c+1,i+1,first,s[i])
#                 b=solve(c,i+1,first,second)
#             return a+b
#         n=len(s)
#         c=0
#         i=0
#         return solve(c,i,-1,-1)%int(1e9+7)
        # n=len(s)
        # ans=0
        # dp=[[[[0 for j in range(10)] for k in range(10)] for p in range(n+1)] for i in range(6)]
        # for c in range(5,-1,-1):
        #     for i in range(n-1,-1,-1):
        #         for first in range(10):
        #             for second in range(10):
        #                     if(c==5):
        #                         dp[c][i][first][second]=1
        #                     else:
        #                         if(c==0):
        #                             a=dp[c+1][i+1][int(s[i])][second]
        #                             b=dp[c][i+1][first][second]
        #                         elif(c==1):
        #                             a=dp[c+1][i+1][first][int(s[i])]
        #                             b=dp[c][i+1][first][second]
        #                         elif(c==2):
        #                             a=dp[c+1][i+1][first][second]
        #                             b=dp[c][i+1][first][second]
        #                         elif(c==3):
        #                             a=0
        #                             if(int(s[i])==second):
        #                                 a=dp[c+1][i+1][first][second]
        #                             b=dp[c][i+1][first][second]
        #                         elif(c==4):
        #                             a=0
        #                             if(int(s[i])==first):
        #                                 a=dp[c+1][i+1][first][second]
        #                             b=dp[c][i+1][first][second]
        #                         dp[c][i][first][second]=a+b
        #                     ans=max(ans,dp[c][i][first][second])
        # print(ans)
        # return dp[c][0][0][0]%int(1e9+7)
        MOD = 10**9 + 7
        res = 0
        dp = [[[[0]*11 for i in range(11)] for i in range(11)] for i in range(11)]
        for x in s:
            i = ord(x) - ord('0')
            for j in range(10):
                for k in range(10):
                    res =(res+dp[i][j][k][j])%MOD
                    dp[j][i][k][i] += dp[j][i][k][10]
                    dp[j][k][i][10] += dp[j][k][10][10]
                dp[j][i][10][10] += dp[j][10][10][10];
            dp[i][10][10][10] +=1
        return res

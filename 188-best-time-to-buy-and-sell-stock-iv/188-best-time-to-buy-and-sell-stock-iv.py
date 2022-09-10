class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def solve(i,c,t):
            if(i>=n):
                return 0
            if(t>=k):
                return 0
            a1=0
            a2=0
            b1=0
            b2=0
            if(c==0):
                a1=solve(i+1,c^1,t)-prices[i]
                a2=solve(i+1,c,t)
            else:
                b1=solve(i+1,c^1,t+1)+prices[i]
                b2=solve(i+1,c,t)
            return max(a1,a2,b1,b2)
        n=len(prices)
        return solve(0,0,0)
sys.setrecursionlimit(1000000)
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n=len(nextVisit)
        dp=[0 for i in range(n)]
        for i in range(1,n):
            dp[i]=dp[i-1]+dp[i-1]-dp[nextVisit[i-1]]+2
        return dp[-1]%int(1e9+7)
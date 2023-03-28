class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def solve(i,limit):
            if(i>=n):
                return 0
            x=days[i]-limit
            if(x>0):
                a=solve(i+1,days[i])+costs[0]
                b=solve(i+1,days[i]+6)+costs[1]
                c=solve(i+1,days[i]+29)+costs[2]
                return min(a,b,c)
            else:
                return solve(i+1,limit)
        n=len(days)
        return solve(0,0)
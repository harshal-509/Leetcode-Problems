class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        @cache
        def solve(i):
            if(i>=n):
                return 0
            if(n-i==1):
                return piles[i]
            s=-float('inf')
            t=suff[i]
            for j in range(1,4):
                op=solve(i+j)
                s=max(s,t-op)
            return s
        n=len(piles)
        suff=[0 for i in range(n)]
        suff[-1]=piles[-1]
        for i in range(n-2,-1,-1):
            suff[i]=piles[i]+suff[i+1]
        x=solve(0)
        t=sum(piles)
        if(t-x>x):
            return "Bob"
        elif(t-x<x):
            return "Alice"
        return "Tie"
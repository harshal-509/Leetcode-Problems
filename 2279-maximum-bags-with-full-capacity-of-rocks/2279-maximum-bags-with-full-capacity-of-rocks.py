class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n=len(rocks)
        t=[0 for i in range(n)]
        for i in range(n):
            t[i]=capacity[i]-rocks[i]
        ans=0
        t.sort()
        for i in range(n):
            if(additionalRocks>=t[i]):
                additionalRocks-=t[i]
                t[i]=0
                ans+=1
            else:
                break
        print(t)
        return ans
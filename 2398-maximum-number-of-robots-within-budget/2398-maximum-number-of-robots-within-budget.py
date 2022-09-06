from sortedcontainers import SortedList
class MaxHeapObj:
    def __init__(self,val): self.val = val
    def __lt__(self,other): return self.val > other.val
    def __eq__(self,other): return self.val == other.val
    def __str__(self): return str(self.val)
class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self, x): heapq.heappush(self.h, x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self, i): return self.h[i]
    def __len__(self): return len(self.h)
class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self, i): return self.h[i].val
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        #TLE  
        # def check(i,j,h):
        #     t=h.heappop()
        #     h.heappush(t)
        #     if(t[0]+(j-i+1)*getsum(i,j)>budget):
        #         return 1
        #     return 0
        # def getsum(l,r):
        #     if l == 0:
        #         return prefix[r]
        #     return prefix[r] - prefix[l - 1]
        # ans=0
        # n=len(runningCosts)
        # prefix=[0 for i in range(n)]
        # prefix[0]=runningCosts[0]
        # h=MaxHeap()
        # for i in range(1,n):
        #     prefix[i]+=prefix[i-1]+runningCosts[i]
        # i=0
        # j=0
        # while(j<n):
        #     h.heappush([chargeTimes[j],j])
        #     x=check(i,j,h)
        #     if(x):
        #         while(i<=j and check(i,j,h)):
        #             y=h.heappop()
        #             if(y[1]<=i):
        #                 pass
        #             else:
        #                 h.heappush(y)
        #             i+=1
        #     ans=max(ans,j-i+1)
        #     j+=1
        # ans=max(ans,j-i)
        # return ans
        
        i=0
        j=0
        n=len(chargeTimes)
        s=SortedList()
        cur=0
        ans=0
        while(j<n):
            cur+=runningCosts[j]
            s.add(chargeTimes[j])
            if(s[-1]+(j-i+1)*cur>budget):
                s.remove(chargeTimes[i])
                cur-=runningCosts[i]
                i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans
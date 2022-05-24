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
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h=MinHeap()
        n=len(nums)
        m=len(nums[0])
        mi=float('inf')
        ma=-float('inf')
        for i in range(n):
            h.heappush([nums[i][0],(i,1,len(nums[i]))])
            mi=min(mi,nums[i][0])
            ma=max(ma,nums[i][0])
        ans=[mi,ma]
        while(h):
            z=h.heappop()
            if(len(h)==n-1 and ma-z[0]<ans[1]-ans[0]):
                ans=[z[0],ma]
            if(z[1][1]<z[1][2]):
                h.heappush([nums[z[1][0]][z[1][1]],(z[1][0],z[1][1]+1,z[1][2])])
                ma=max(ma,nums[z[1][0]][z[1][1]])
        return ans
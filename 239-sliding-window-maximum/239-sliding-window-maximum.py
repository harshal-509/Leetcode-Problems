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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h=MaxHeap()
        ans=[]
        n=len(nums)
        for i in range(k):
            h.heappush((nums[i],i))
        x=h.heappop()
        ans.append(x[0])
        h.heappush(x)
        for i in range(k,n):
            x=nums[i]
            y=h.heappop()
            while(h and y[1]<=i-k):
                y=h.heappop()
            if(x<y[0] and y[1]>i-k):
                ans.append(y[0])
                h.heappush(y)
                h.heappush((x,i))
            else:
                a=(x,i)
                ans.append(x)
                h.heappush(a)
        return ans
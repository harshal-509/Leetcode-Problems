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
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        h=MaxHeap()
        for i in range(n):
            h.heappush(stones[i])
        while(h):
            x=h.heappop()
            if(h):
                y=h.heappop()
                if(x==y):
                    pass
                else:
                    h.heappush(abs(x-y))
            else:
                h.heappush(x)
                break
        if(h):
            return h[0]
        return 0
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
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses=sorted(courses,key=lambda x:x[1])
        h=MaxHeap()
        i=0
        t=0
        ans=0
        n=len(courses)
        while(i<n):
            if(courses[i][0]+t>courses[i][1]):
                if(h):
                    x=h.heappop()
                    t-=x
                    t+=min(x,courses[i][0])
                    h.heappush(min(x,courses[i][0]))
            else:
                h.heappush(courses[i][0])
                t+=courses[i][0]
            i+=1
            ans=max(ans,len(h))
        return ans
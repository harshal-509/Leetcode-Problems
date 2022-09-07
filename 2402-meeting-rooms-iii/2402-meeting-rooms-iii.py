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
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        i=0
        t=0
        m=len(meetings)
        meetings.sort()
        for i in range(m):
            t=max(t,meetings[i][1])
        rooms=[0 for i in range(n)]
        count=[0 for i in range(n)]
        delay=[0 for i in range(n)]
        q=deque(meetings)
        s=0
        h=MinHeap()
        j=0
        k=0
        while(k<m):
            while(h):
                x=h.heappop()
                if(x[0]<=meetings[k][0]):
                    rooms[x[1]]=0
                    s-=1
                else:
                    h.heappush(x)
                    break
            if(s==n):
                x=h.heappop()
                rooms[x[1]]=0
                s-=1
            for i in range(n):
                if(rooms[i]==0):
                    rooms[i]=1
                    count[i]+=1
                    if(delay[i]>meetings[k][0]):
                        h.heappush([delay[i]-meetings[k][0]+meetings[k][1],i])
                        delay[i]=delay[i]-meetings[k][0]+meetings[k][1]
                    else:
                        h.heappush([meetings[k][1],i])
                        delay[i]=meetings[k][1]
                    s+=1
                    break
            k+=1
        a=0
        ans=0
        for i in range(n):
            if(count[i]>a):
                ans=i
                a=count[i]
        return ans
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
class LRUCache:
    def __init__(self, capacity: int):
        self.t=0
        self.z=Counter([])
        self.p=MinHeap()
        self.c=capacity
        self.o=0
        self.q=0
        self.a=Counter([])
    def get(self, key: int) -> int:
        if(self.z[key]):
            self.p.heappush([self.o,key])
            self.a[key]=self.o
            self.o+=1
            return self.z[key]-1
        return -1
    def put(self, key: int, value: int) -> None:
        if(self.q<self.c):
            if(self.z[key]):
                self.z[key]=value+1
                self.p.heappush([self.o,key])
                self.a[key]=self.o
                self.o+=1
            else:
                self.z[key]=value+1
                self.p.heappush([self.o,key])
                self.a[key]=self.o
                self.o+=1
                self.q+=1
        else:
            if(self.z[key]):
                self.z[key]=value+1
                self.p.heappush([self.o,key])
                self.a[key]=self.o
                self.o+=1
            else:
                while(self.p):
                    a=self.p.heappop()
                    if(self.a[a[1]]==a[0]):
                        break
                self.z[a[1]]=0
                self.a[a[1]]=float('inf')
                self.z[key]=value+1
                self.p.heappush([self.o,key])
                self.a[key]=self.o
                self.o+=1
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
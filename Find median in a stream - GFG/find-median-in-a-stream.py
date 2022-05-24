#{ 
#Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


 # } Driver Code Ends
#User function Template for python3
''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''
import heapq
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
    def __init__(self):
        self.mi=MinHeap()
        self.ma=MaxHeap()
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        x=len(self.mi)
        y=len(self.ma)
        if(x==y):
            return
        if(abs(x-y)==1):
            if(y-1==x):
                return
            self.ma.heappush(self.mi.heappop())
        if(abs(x-y)==2):
            if(x==y-2):
                self.mi.heappush(self.ma.heappop())
            else:
                self.ma.heappush(self.mi.heappop())
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if((len(self.mi)+len(self.ma))%2):
            return self.ma[0]
        return (self.ma[0]+self.mi[0])/2
    def insertHeaps(self,x):
        #:param x: value to be inserted
        #:return: None
        # code here
        if(self.ma and self.ma[0]<=x):
            self.mi.heappush(x)
        else:
            self.ma.heappush(x)
        self.balanceHeaps()
#{ 
#Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

#} Driver Code Ends
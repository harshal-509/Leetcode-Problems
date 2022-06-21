class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i=0
        n=len(heights)
        arr=[]
        h=heapq.heapify(arr)
        for i in range(n-1):
            x=heights[i+1]-heights[i]
            if(x>0):
                heapq.heappush(arr,x)
                if(len(arr)>ladders):
                    bricks-=heapq.heappop(arr)
                    if(bricks<0):
                        return i
        return i+1
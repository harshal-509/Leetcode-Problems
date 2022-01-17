class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        i=0
        n=len(intervals)
        while(i<n-1):
            if(intervals[i][1]>=intervals[i+1][0]):
                intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals.remove(intervals[i+1])
                n-=1
            else:
                i+=1 
        return intervals
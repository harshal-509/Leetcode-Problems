class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i=0
        n=len(intervals)
        ans=n
        while(i<n-1):
            if(intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]):
                ans-=1
                intervals[i+1][0]=intervals[i][0]
                intervals[i+1][1]=intervals[i][1]
            elif(intervals[i][0]==intervals[i+1][0] and intervals[i+1][1]>=intervals[i+1][1]):
                ans-=1
                intervals[i+1][0]=intervals[i][0]       
                intervals[i+1][1]=intervals[i+1][1]
            i+=1
        return ans
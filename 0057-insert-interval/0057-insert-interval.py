class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        n=len(intervals)
        flag=0
        if(n==0):
            intervals.append(newInterval)
            return intervals
        if(n==1):
            if(intervals[i][1]>=newInterval[0] and intervals[i][0]<=newInterval[0]):
                intervals[i][0]=min(intervals[i][0],newInterval[0])
                intervals[i][1]=max(intervals[i][1],newInterval[1])
                flag=1
        while(i<n-1):
            if(intervals[i][1]>=intervals[i+1][0]):
                intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals.remove(intervals[i+1])
                n-=1
            elif(intervals[i][1]>=newInterval[0] and intervals[i][0]<=newInterval[0] and flag==0):
                intervals[i][0]=min(intervals[i][0],newInterval[0])
                intervals[i][1]=max(intervals[i][1],newInterval[1])
                flag=1
            else:
                i+=1
        if(flag==0):
            if(newInterval[0]>intervals[-1][1]):
                intervals.append(newInterval)
            else:
                intervals.insert(0,newInterval)
                i=0
                intervals.sort()
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
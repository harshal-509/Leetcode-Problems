class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        ans=0
        tasks.sort()
        processorTime.sort()
        j=len(tasks)-1
        i=0
        while(i<len(processorTime)):
            count=0
            while(j>=0 and count<4):
                ans=max(ans,processorTime[i]+tasks[j])
                j-=1
                count+=1
            i+=1
        return ans
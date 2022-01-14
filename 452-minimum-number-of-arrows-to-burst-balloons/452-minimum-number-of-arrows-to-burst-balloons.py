class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        print(points)
        i=0
        j=1
        ans=1
        n=len(points)
        while(i<n and j<n):
            if(points[i][1]<points[j][0]):
                ans+=1
                i=j
                j+=1
            else:
                j+=1
        return ans
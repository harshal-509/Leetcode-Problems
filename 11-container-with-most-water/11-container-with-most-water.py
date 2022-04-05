class Solution:
    def maxArea(self, height: List[int]) -> int:
        m=0
        n=len(height)
        i=0
        j=n-1
        while(i<j):
            m=max(m,(j-i)*min(height[i],height[j]))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return m
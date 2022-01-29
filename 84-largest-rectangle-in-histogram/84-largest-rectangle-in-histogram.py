class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[0 for i in range(n)]
        right=[0 for i in range(n)]
        s=[]
        for i in range(n):
            if(s):
                while(s and heights[s[-1]]>=heights[i]):
                    s.pop()
                if(s):
                    left[i]=s[-1]+1
                    s.append(i)
                else:
                    s.append(i)
                    left[i]=0
            else:
                s.append(0)
                left[i]=0
        s=[]
        for i in range(n-1,-1,-1):
            if(s):
                while(s and heights[s[-1]]>=heights[i]):
                    s.pop()
                if(s):
                    right[i]=s[-1]-1
                    s.append(i)
                else:
                    s.append(i)
                    right[i]=n-1
            else:
                s.append(n-1)
                right[i]=n-1
        ans=0
        for i in range(n):
            ans=max(ans,(right[i]-left[i]+1)*heights[i])
        return ans
                
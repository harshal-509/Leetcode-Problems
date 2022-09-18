class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=0
        n=len(height)
        i=0
        j=n-1
        ans=0
        while(i<=j):
            if(height[i]<=height[j]):
                if(left>=height[i]):
                    ans+=left-height[i]
                else:
                    left=height[i]
                i+=1
            else:
                if(right>=height[j]):
                    ans+=right-height[j]
                else:
                    right=height[j]
                j-=1
        return ans
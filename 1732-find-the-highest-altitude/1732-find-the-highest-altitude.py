class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        n=len(gain)
        temp=0
        for i in range(n):
            temp+=gain[i]
            ans=max(ans,temp)
        return ans
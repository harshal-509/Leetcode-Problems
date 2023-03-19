class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        z=Counter([])
        for i in nums:
            z[i%value]+=1
        ans=-1
        n=len(nums)
        for i in range(n):
            if(z[i%value]):
                z[i%value]-=1
            else:
                return i
        return n
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def solve(i):
            if(i>=n):
                return 1
            a=0
            if(not(temp) or not(nums[i]+k in temp or nums[i]-k in temp)):
                temp.append(nums[i])
                a=solve(i+1)
                temp.pop()
            b=solve(i+1)
            return a+b
        temp=[]
        n=len(nums)
        return solve(0)-1
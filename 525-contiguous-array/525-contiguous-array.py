class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        z=defaultdict(list)
        t=0
        ans=0
        n=len(nums)
        z[0]=[-1]
        for i in range(n):
            if(nums[i]==0):
                t+=1
            else:
                t-=1
            if(z[t]):
                ans=max(ans,i-z[t][0])
            z[t].append(i)
        return ans
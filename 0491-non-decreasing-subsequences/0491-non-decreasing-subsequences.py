class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def solve(i):
            if(len(temp)>=2):
                x=tuple(temp.copy())
                if(z[x]==0):
                    ans.append(x)
                    z[x]+=1
            if(i>=n):
                return 
            if(nums[i]>=temp[-1]):
                temp.append(nums[i])
                solve(i+1)
                temp.pop()
            solve(i+1)
        n=len(nums)
        ans=[]
        z=Counter([])
        for i in range(n):
            temp=[nums[i]]
            solve(i+1)
            temp.pop()
        return ans
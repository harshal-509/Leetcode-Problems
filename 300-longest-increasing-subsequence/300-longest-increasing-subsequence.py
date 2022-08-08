class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[]
        sol=0
        for i in nums:
            if(ans):
                if(ans[-1]<i):
                    ans.append(i)
                else:
                    x=bisect_left(ans,i)
                    ans[x]=i
            else:
                ans.append(i)
            sol=max(sol,len(ans))
        return sol
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        z=Counter(nums)
        for i in range(1,n+1):
            if(z[i]==2):
                ans=i
            if(z[i]==0):
                ans1=i
        return [ans,ans1]
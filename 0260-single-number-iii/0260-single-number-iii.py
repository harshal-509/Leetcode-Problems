class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        z=Counter(nums)
        ans=[]
        for i in z:
            if(z[i]==1):
                ans.append(i)
        return ans
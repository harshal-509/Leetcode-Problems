class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=0
        for i in nums:
            if(i%2==0):
                s+=i
        ans=[]
        for i in queries:
            x=nums[i[1]]
            nums[i[1]]+=i[0]
            if(nums[i[1]]%2==0):
                if(x%2==0):
                    s+=nums[i[1]]-x
                else:
                    s+=nums[i[1]]
            else:
                if(x%2==0):
                    s-=x
            ans.append(s)
        return ans
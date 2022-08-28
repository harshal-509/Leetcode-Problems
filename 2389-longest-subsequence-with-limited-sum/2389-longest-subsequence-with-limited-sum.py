class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        for i in range(1,n):
            nums[i]+=nums[i-1]
        ans=[]
        for i in queries:
            x=0
            for j in nums:
                if(i>=j):
                    x+=1
                else:
                    break
            ans.append(x)
        return ans
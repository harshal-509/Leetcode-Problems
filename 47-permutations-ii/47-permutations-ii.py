class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def hs(nums,i,temp,ans):
            if(i==n):
                if(temp not in ans):
                    ans.append(temp.copy())
                return
            for j in range(i,n):
                nums[i],nums[j]=nums[j],nums[i]
                temp.append(nums[i])
                hs(nums,i+1,temp,ans)
                temp.pop()
                nums[i],nums[j]=nums[j],nums[i]
        ans=[]
        hs(nums,0,[],ans)
        return ans
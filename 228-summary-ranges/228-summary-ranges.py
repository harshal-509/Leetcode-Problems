class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        n=len(nums)
        if(n==0):
            return []
        a=nums[0]
        b=a
        for i in range(1,n):
            if(nums[i]-a==1):
                a=nums[i]
            else:
                if(a!=b):
                    ans.append(str(b)+"->"+str(a))
                    b=nums[i]
                    a=b
                else:
                    ans.append(str(b))
                    b=nums[i]
                    a=b
        if(a!=b):
            ans.append(str(b)+"->"+str(a))
        else:
            ans.append(str(b))
        return ans
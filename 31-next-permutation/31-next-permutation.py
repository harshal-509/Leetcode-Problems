class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        flag=1
        for i in range(n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                flag=0
                index=i
                break
        if(flag):
            nums.sort()
        else:
            j=nums[index+1]
            k=index+1
            for i in range(index+1,n):
                if(nums[i]<=j and nums[i]>nums[index]):
                    k=i
            nums[index],nums[k]=nums[k],nums[index]
            i=index+1
            j=n-1
            while(i<=j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
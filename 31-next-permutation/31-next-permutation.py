class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        index=-1
        for i in range(n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                index=i
                break
        if(index==-1):
            nums.sort()
            return nums
        index1=i+1
        for i in range(index+1,n):
            if(nums[i]<=nums[index1] and nums[i]>nums[index]):
                index1=i
        nums[index1],nums[index]=nums[index],nums[index1]
        i=index+1
        j=n-1
        while(i<j):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return nums
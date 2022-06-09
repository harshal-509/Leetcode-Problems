class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        i=0
        j=n-1
        while(i<j):
            if(numbers[i]+numbers[j]==target):
                return [i+1,j+1]
            if(numbers[i]+numbers[j]<target):
                i+=1
            else:
                j-=1
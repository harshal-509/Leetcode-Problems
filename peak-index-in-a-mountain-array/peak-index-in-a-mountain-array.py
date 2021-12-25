class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i=1
        j=len(arr)-2
        #[0,2,3,1,0]
        while(i<=j):
            m=(i)+(j-i)//2
            if(arr[m]>arr[m+1] and arr[m]>arr[m-1]):
                return m
            elif(arr[m]<arr[m+1]):
                i=m+1
            elif(arr[m]<arr[m-1]):
                j=m-1
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        k=len(arr)
        if(k<3):
            return 0
        else:
            i=0
            a=arr[i+1]
            j=k-1
            b=arr[j-1]
            while(arr[i]<a and i<k-2):
                i+=1
                a=arr[i+1]
            while(b>arr[j] and j>1):
                j-=1
                b=arr[j-1]
        return i==j
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        i=0
        j=n
        while(i<j):
            m=i+(j-i)//2
            if(arr[m]-m-1<k):
                i=m+1
            else:
                j=m
        return j+k
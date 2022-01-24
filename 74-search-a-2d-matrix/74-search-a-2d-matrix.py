class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        i=0
        j=n-1
        index=-1
        while(i<=j):
            mid=i+(j-i)//2
            if(matrix[mid][0]>target):
                j=mid-1
            else:
                index=mid
                i=mid+1
        i=0
        j=m-1
        if(index==-1):
            return False
        while(i<=j):
            mid=i+(j-i)//2
            if(matrix[index][mid]==target):
                return True
            elif(matrix[index][mid]>target):
                j=mid-1
            else:
                i=mid+1
        return False
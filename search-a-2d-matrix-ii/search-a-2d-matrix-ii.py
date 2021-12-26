class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=0
        c=len(matrix[0])-1
        n=len(matrix)
        while(r<n and c>=0):
            x=matrix[r][c]
            if(target==x):
                return 1
            elif(target<x):
                c-=1
            else:
                r+=1
        return 0

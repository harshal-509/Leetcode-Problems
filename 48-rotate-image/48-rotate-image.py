class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            k=0
            j=n-1
            while(k<j):
                matrix[i][k],matrix[i][j]=matrix[i][j],matrix[i][k]
                k+=1
                j-=1
                
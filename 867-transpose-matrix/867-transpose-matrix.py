class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        transpose=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(matrix[j][i])
            transpose.append(temp)
        return transpose
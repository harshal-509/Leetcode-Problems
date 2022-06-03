class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n=len(matrix)
        m=len(matrix[0])
        self.pre=[[0 for j in range(m)] for i in range (n)]
        for i in range(n):
            self.pre[i][0]=matrix[i][0]
        for i in range(n):
            for j in range(1,m):
                self.pre[i][j]+=self.pre[i][j-1]+matrix[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for i in range(row1,row2+1):
            if(col1-1>=0):
                ans+=self.pre[i][col2]-self.pre[i][col1-1]
            else:
                ans+=self.pre[i][col2]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ans=[[-1 for i in range(n-2)] for j in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                temp=0
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        temp=max(temp,grid[x][y])
                ans[i][j]=temp
        return ans
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        row_trans = k // m
        for i in range(row_trans):
            grid = [ grid[n-1] ] + grid[:n-1]

        k = k % m

        arr = [ grid[i][j] for i in range(n) for j in range(m)]

        arr = arr[-k:] + arr[:-k]
        grid = []
        for i in range(n):
            grid.append(arr[m*i:m*(i+1)])
        return grid
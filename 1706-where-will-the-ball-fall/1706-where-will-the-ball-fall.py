class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def move_ball(j):
            for i in range(m):
                k = j + grid[i][j]
                if not (0 <= k < n) or (grid[i][k] != grid[i][j]):
                    return -1
                j = k
            return j
        return [move_ball(j) for j in range(n)]
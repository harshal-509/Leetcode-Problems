class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[float("-inf")] * n for _ in range(n)]
        dp[0][n - 1] = grid[0][0] + grid[0][n - 1] - int(n == 1) * grid[0][0]
        for i in range(1, m):
            prev, dp = dp, [[float("-inf")] * n for _ in range(n)]
            for j in range(n):
                for c in range(n):
                    for s1, s2 in itertools.product([-1, 0, 1], repeat=2):
                        if 0 <= j + s1 <= n - 1 and 0 <= c + s2 <= n - 1:
                            dp[j][c] = max(dp[j][c], prev[j + s1][c + s2])
                    dp[j][c] += grid[i][j] + grid[i][c] * (j != c)
        ans=0
        for i in dp:
            ans=max(ans,max(i))
        return ans
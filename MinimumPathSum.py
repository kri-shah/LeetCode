class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        dp = grid[0]
        for c in range(1, COLS):
            dp[c] += dp[c - 1]
        
        for r in range(1, ROWS):
            curr = [0] * COLS
            for c in range(COLS):
                if c == 0:
                    curr[c] = grid[r][c] + dp[c]
                else:
                    curr[c] = grid[r][c] + min(dp[c], curr[c - 1])
            dp = curr
        
        return dp[-1]

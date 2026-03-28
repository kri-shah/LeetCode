class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)        
        COLS = len(matrix[0])

        dp = matrix[0][:]
        
        for r in range(1, ROWS):
            curr = [0] * COLS
            for c in range(COLS):
                if c == 0:
                    curr[c] = matrix[r][c] + min(dp[c], dp[c + 1])
                elif c == COLS - 1:
                    curr[c] = matrix[r][c] + min(dp[c], dp[c - 1])
                else:
                    curr[c] = matrix[r][c] + min(dp[c], dp[c - 1], dp[c + 1])
            dp = curr[:]
        
        return min(dp)

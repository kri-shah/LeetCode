class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        row_prefix = [[0] * (COLS + 1) for _ in range(ROWS)]  
        for r in range(ROWS):
            for c in range(COLS):
                row_prefix[r][c+1] = grid[r][c] + row_prefix[r][c]
        
        col_prefix = [[0] * (COLS) for _ in range(ROWS + 1)]
        for c in range(COLS):
            for r in range(ROWS):
                col_prefix[r+1][c] = grid[r][c] + col_prefix[r][c]
        
        diag1_prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            for c in range(COLS):
                diag1_prefix[r+1][c+1] = grid[r][c]+ diag1_prefix[r][c]
        
        diag2_prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            for c in range(COLS - 1, -1, -1):
                diag2_prefix[r+1][c] =  grid[r][c] + diag2_prefix[r][c+1]

        def largest_square(i, j):
            max_k = min(ROWS - i, COLS - j) 

            for k in range(max_k, 1, -1):
                target = diag1_prefix[i+k][j+k] - diag1_prefix[i][j]
                diag2 = diag2_prefix[i+k][j] - diag2_prefix[i][j+k]
                if diag2 != target:
                    continue
                ok = True
                for r in range(i, i + k):
                    if row_prefix[r][j+k] - row_prefix[r][j] != target:
                        ok = False
                        break
                
                if not ok:
                    continue
                
                for c in range(j, j + k):
                    if col_prefix[i+k][c] - col_prefix[i][c] != target:
                        ok = False
                        break

                if ok:
                    return k

            return 1
        
        res = 1
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, largest_square(r, c))
        
        return res

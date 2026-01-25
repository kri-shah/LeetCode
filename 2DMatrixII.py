class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        r, c = 0, COLS - 1

        while r < ROWS and c >= 0:
            pos = matrix[r][c]
            if pos == target:
                return True
            elif target < pos:
                c -= 1
            else:
                r += 1
        
        return False

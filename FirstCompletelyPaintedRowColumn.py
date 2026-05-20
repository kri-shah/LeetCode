class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])

        mapping = dict()
        for r in range(ROWS):
            for c in range(COLS):
                mapping[mat[r][c]] = (r, c)
            
        marked_rows = [0] * ROWS
        marked_cols = [0] * COLS

        for i, num in enumerate(arr):
            r, c = mapping[num]
            marked_rows[r] += 1
            marked_cols[c] += 1
            if marked_rows[r] == COLS or marked_cols[c] == ROWS:
                return i

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:        
        def transpose(box):
            ROWS, COLS = len(box), len(box[0])
            transposed = [[0 for _ in range(ROWS)] for _ in range(COLS)]
            
            for r in range(ROWS):
                for c in range(COLS):
                    transposed[c][r] = box[r][c]
            for r in range(COLS):
                transposed[r] = transposed[r][::-1]
            
            return transposed
        
        transposed = transpose(boxGrid)
        
        ROWS, COLS = len(transposed), len(transposed[0])

        for c in range(COLS):
            bottom = ROWS - 1
            for r in range(ROWS - 1, -1, -1):
                if transposed[r][c] == '#':
                    transposed[r][c] = '.'
                    transposed[bottom][c] = '#'
                    bottom -= 1
                elif transposed[r][c] == '*':
                    bottom = r - 1

        return transposed
            

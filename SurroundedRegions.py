class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(pos):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
            stack = [pos]
            while stack:
                print(stack)
                i, j = stack.pop()
                
                board[i][j] = '#'
                for x, y in directions:
                    newr, newc = i + x, j + y
                    
                    if (newr >= 0 and newr < ROWS 
                    and newc >= 0 and newc < COLS 
                    and board[newr][newc] == 'O'):
                        stack.append((newr, newc))
                        
        for c in [0, COLS - 1]:
            for r in range(ROWS):
                if board[r][c] == 'O':
                    dfs((r, c))
        
        for r in [0, ROWS - 1]:
            for c in range(COLS):
                if board[r][c] == 'O':
                    dfs((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'



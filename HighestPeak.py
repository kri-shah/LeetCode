class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        res = [['#' for _ in range(COLS)] for _ in range(ROWS)]
        
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    res[r][c] = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            q_len = len(queue)
            
            for _ in range(q_len):
                x, y = queue.popleft()
                
                for i, j in directions:
                    newr, newc = x + i, y + j
                    if (newr >= 0 and newr < ROWS
                    and newc >= 0 and newc < COLS):
                        if res[newr][newc] == '#':
                            res[newr][newc] = res[x][y] + 1
                            queue.append((newr, newc))
        
        return res

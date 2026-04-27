class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: {(0, 1), (0, -1)},
            2: {(1, 0), (-1, 0)},
            3: {(1, 0), (0, -1)},
            4: {(1, 0), (0, 1)},
            5: {(-1, 0), (0, -1)},
            6: {(-1, 0), (0, 1)}
        }

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            r, c = queue.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return True

            for dx, dy in directions[grid[r][c]]:
                nr, nc = r + dx, c + dy

                if (0 <= nr < ROWS and 0 <= nc < COLS 
                    and (nr, nc) not in visited
                    and (-dx, -dy) in directions[grid[nr][nc]]):
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return False

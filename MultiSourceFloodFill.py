class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        res = [[0 for _ in range(m)] for _ in range(n)]
        
        queue = deque()
        visited = set()

        for x, y, color in sources:
            queue.append((x, y))
            res[x][y] = max(res[x][y], color)
            visited.add((x, y))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            level = set()
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    newr, newc = x + dx, y + dy
                    if (newr >= 0 and newr < n 
                        and newc >= 0 and newc < m 
                        and (newr, newc) not in visited):
                            res[newr][newc] = max(res[newr][newc], res[x][y])
                            level.add((newr, newc))
            for x, y in level:
                visited.add((x, y))
                queue.append((x,y))
        return res

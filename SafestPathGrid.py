class Solution:    
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[0 for _ in range(n)] for _ in range(n)]
        visited = set()
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visited.add((r, c))

        print(dist)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                r, c = queue.popleft()
                for i, j in directions:
                    newr, newc = r + i, c + j
                    if (newr >= 0 and newr < n 
                    and newc >= 0 and newc < n
                    and (newr, newc) not in visited):
                        dist[newr][newc] = dist[r][c] + 1
                        visited.add((newr, newc))
                        queue.append((newr, newc))
        
        visited = set()
        heap = []
        heapq.heappush(heap, [dist[0][0] * -1, (0, 0)])
        while heap:
            cost, (r, c) = heapq.heappop(heap)
            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return cost * -1
            for i, j in directions:
                newr, newc = r + i, c + j
                if (newr >= 0 and newr < n 
                and newc >= 0 and newc < n
                and (newr, newc) not in visited):
                    new_cost = min(cost * -1, dist[newr][newc])
                    heapq.heappush(heap, [new_cost * -1, (newr, newc)])
        
        

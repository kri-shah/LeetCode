import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = float('inf')
        
        heap = []
        heapq.heappush(heap, (0, (0, 0)))
        visited = set()
        
        while heap:
            cost, (x, y) = heapq.heappop(heap)
            
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            
            if x == ROWS - 1 and y == COLS - 1:
                return cost
            
            for i, j in directions:
                newr, newc = x + i, y + j
                if (newr >= 0 and newr < ROWS
                and newc >= 0 and newc < COLS and (newr, newc) not in visited):
                    new_cost = max(cost, abs(heights[x][y] - heights[newr][newc]))
                    heapq.heappush(heap, (new_cost, (newr, newc)))

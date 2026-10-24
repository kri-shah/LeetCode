class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        heap = []
        heapq.heappush(heap, (-1, start_node))
        visited = set([start_node])
        while heap:
            cost, node = heapq.heappop(heap)
            if node == end_node:
                return -cost
            
            visited.add(node)
            for neigh, neigh_cost in graph[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (cost * neigh_cost, neigh))

        return 0.0

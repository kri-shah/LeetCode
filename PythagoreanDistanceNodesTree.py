class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(start):
            dist = [-1] * n
            queue = deque([start])
            
            dist[start] = 0
            
            while queue:
                node = queue.popleft()
                for neigh in graph[node]:
                    if dist[neigh] != -1:
                        continue
                    dist[neigh] = dist[node] + 1
                    queue.append(neigh)

            return dist

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        res = 0
        for i in range(n):
            a, b, c = sorted([dx[i], dy[i], dz[i]])
            if a ** 2 + b ** 2 == c ** 2:
                res +=1

        return res

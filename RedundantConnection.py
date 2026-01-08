from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        def dfs(cur, prev):
            if cur in visited:
                return True
            
            visited.add(cur)
            for neigh in graph[cur]:
                if neigh == prev:
                    continue
                if dfs(neigh, cur):
                    return True
            return False
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visited = set()
            if dfs(u, -1):
                return [u, v]

        return []


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j]:
                    graph[i].append(j)

        visited = set()
        def dfs(i):
            stack = [i]
            visited.add(i)
            while stack:
                pos = stack.pop()
                for neigh in graph[pos]:
                    if neigh not in visited:
                        visited.add(neigh)
                        stack.append(neigh)
        
        provinces = 0
        for i in range(n):
            if i not in visited:
                provinces += 1
                dfs(i)
        
        return provinces

class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        from collections import defaultdict

        tree = defaultdict(list)
        for par, child in edges:
            tree[par].append(child)

        def dfs(node):
            if node not in tree:
                return baseTime[node]
            
            mx = float('-inf')
            mi = float('inf')
            for child in tree[node]:
                recur = dfs(child)
                mx = max(mx, recur)
                mi = min(mi, recur)
            
            own = (mx - mi) + baseTime[node]
            return mx + own
        
        return dfs(0)

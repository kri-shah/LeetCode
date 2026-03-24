class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        cycle = set()
        def has_cycle(node, par):
            if node in cycle:
                return True
            cycle.add(node)
            for neigh in tree[node]:
                if neigh == par:
                    continue
                if has_cycle(neigh, node):
                    return True
            
            return False


        return not has_cycle(0, -1) and len(cycle) == n


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # [2,  5,   5,  1,  2,  20]
        # ["a","b","c","c","e","d"]
        # ["b","c","b","e","b","e"]
        #   2
        # a -> b
        dist = [[float('inf') for _ in range(26)] for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
        
        a = ord('a')
        for u, v, c in zip(original, changed, cost):
            dist[ord(u) - a][ord(v) - a] = min(dist[ord(u) - a][ord(v) - a], c)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        total_cost = 0
        for c1, c2 in zip(source, target):
            if dist[ord(c1) - a][ord(c2) - a] == float('inf'):
                return -1
            else:
                total_cost += dist[ord(c1) - a][ord(c2) - a]
        
        return total_cost

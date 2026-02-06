class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        def is_valid(max_weight):
            res = 1
            cur = 0
            for w in weights:
                if cur + w <= max_weight:
                    cur += w
                else:
                    cur = w
                    res += 1
            
            return res <= days
                
        
        while l < r:
            m = (l + r) // 2
            if is_valid(m):        
                r = m
            else:
                l = m + 1
        
        return l

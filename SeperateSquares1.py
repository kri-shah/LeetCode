class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        l = float('inf')
        r = float('-inf')
        
        for _, y, s in squares:
            total += s * s
            l = min(l, y)
            r = max(r, y + s)

        def sum_below(bound):
            a = 0.0
            for _, y, s in squares:
                if bound <= y:
                    continue
                elif bound >= y + s:
                    a += s * s
                else:
                    a += s * (bound - y)
            
            return a

        target = total / 2.0
        res = float('inf')
        eps = 1e-5
        while abs(r - l) > eps:
            m = (l + r) / 2.0
            area = sum_below(m)
            if area >= target:
                r = m 
            else:
                l = m
        
        return r

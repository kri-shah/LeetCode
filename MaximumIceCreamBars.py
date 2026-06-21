class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = cost = 0
        for c in costs:
            cost += c
            if cost <= coins:
                res += 1
            else:
                return res
        
        return res

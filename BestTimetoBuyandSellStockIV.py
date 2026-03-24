class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        
        def dp(i, holding, k_left):
            if i == len(prices):
                return 0
            
            key = (i, holding, k_left)
            if key in memo:
                return memo[key]
            
            memo[key] = dp(i + 1, holding, k_left)
            if not holding:
                memo[key] = max(memo[key], dp(i + 1, True, k_left) - prices[i])
            elif holding and k_left > 0:
                memo[key] = max(memo[key], dp(i + 1, False, k_left - 1) + prices[i])
            
            return memo[key]
        
        return dp(0, False, k)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dp(i, holding, cooldown):
            if i == len(prices):
                return 0
            
            key = (i, holding, cooldown)
            if key in memo:
                return memo[key]
            
            if holding:
                memo[key] = max(dp(i + 1, holding, False), 
                dp(i + 1, False, True) + prices[i])
            else:
                if not cooldown:
                    memo[key] = max(dp(i + 1, False, False),
                        dp(i + 1, True, False) - prices[i])
                else:
                    memo[key] = dp(i + 1, False, False)
            
            return memo[key]
        
        return dp(0, False, False)

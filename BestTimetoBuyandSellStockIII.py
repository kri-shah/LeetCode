class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, holding, transcations_left):
            key = (i, holding, transcations_left)
            if i == len(prices):
                return 0
            if key in memo:
                return memo[key]
            
            memo[key] = dp(i + 1, holding, transcations_left)
            if holding and transcations_left > 0:
                memo[key] = max(
                    memo[key], 
                    dp(i + 1, False, transcations_left - 1) + prices[i]
                )
            elif not holding:
                memo[key] = max(
                    memo[key], 
                    dp(i + 1, True, transcations_left) - prices[i]
                )
            
            return memo[key]
        
        return dp(0, 0, 2)

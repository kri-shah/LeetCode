class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dp(i, can_buy):
            key = (i, can_buy)
            if key in memo: 
                return memo[key]
            if i >= len(prices):
                return 0
            best = dp(i+1, can_buy)
            if can_buy:
                best = max(best, dp(i+1, False) - prices[i])
            else:
                best = max(best, dp(i+2, True) + prices[i])
            memo[key] = best
            
            return memo[key]
        
        return dp(0, True)

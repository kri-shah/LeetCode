def solution(arr):
    total = sum(arr)
    memo = {}
    
    def dp(i, s):
        if i == len(arr):
            return abs(total - s * 2)
        
        key = (i ,s)        
        if key in memo:
            return memo[key]
        
        skip = dp(i + 1, s)
        take = dp(i + 1, s + arr[i])

        memo[key] = min(skip, take)
        return memo[key]
    
    return dp(0, 0)

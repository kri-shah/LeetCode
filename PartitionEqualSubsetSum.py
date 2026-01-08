class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        target = num_sum // 2
        if num_sum % 2 == 1:
            return False
        
        memo = {}
        def dp(i, s):
            key = (i, s)
            if key in memo:
                return memo[key]

            if i == len(nums):
                return s == target
            
            memo[key] = dp(i + 1, s) or dp(i + 1, s + nums[i])
            return memo[key]
        
        return dp(0, 0)

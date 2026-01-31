class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sub_sum = 0
        res = float('inf')
        for r in range(len(nums)):
            sub_sum += nums[r]    
            
            while sub_sum >= target:
                res = min(res, r - l + 1)
                sub_sum -= nums[l]
                l += 1 
        
        return res if res != float('inf') else 0

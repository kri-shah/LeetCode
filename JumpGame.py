class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        
        for i in range(n):
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True
            
            if farthest == i:
                return False
            
        return True

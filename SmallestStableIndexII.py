class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_so_far = float('-inf')
        min_so_far = [float('inf')] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                min_so_far[i] = min(min_so_far[i], nums[i])
            else:
                min_so_far[i] = min(min_so_far[i + 1], nums[i])
        
        for i, num in enumerate(nums):
            max_so_far = max(max_so_far, num)
            if max_so_far - min_so_far[i] <= k:
                return i
                
        return -1

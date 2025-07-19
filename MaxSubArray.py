#accidentally derived Kadane's Alg

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        curmax = float('-inf')
        for i in nums:
            curmax = max(i, curmax + i)
            maxsum = max(maxsum, curmax)
        
        return maxsum

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_n = max(nums)
        
        if max_n <= 2:
            return max_n
        
        ans = 1
        while ans <= max_n:
            ans <<= 1
        return ans

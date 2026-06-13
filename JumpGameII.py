class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        current_reach = nums[0]
        furthest_reach = nums[0]
        res = 1
        
        for i in range(1, n):
            furthest_reach = max(furthest_reach, nums[i] + i)
            if current_reach >= n - 1:
                return res

            if current_reach == i:
                current_reach = furthest_reach 
                res += 1
        
        return res
        

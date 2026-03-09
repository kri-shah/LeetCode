class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums) 
        res = -1
        closest = float('inf')
        
        for i in range(n - 2):
            new_sum = self.two_pointer(i, nums, target)
            if abs(target - new_sum) < closest:
                res = new_sum
                closest = abs(target - new_sum)
            
            if res == target:
                return res
        
        return res
    
    def two_pointer(self, indx, nums, target):
        closest = float('inf')
        res = 0
        l = indx + 1
        r = len(nums) - 1
        
        while l < r:
            curr_sum = nums[l] + nums[r] + nums[indx]
            if abs(target - curr_sum) < closest:
                closest = abs(target - curr_sum)
                res = curr_sum

            if curr_sum < target:
                l += 1
            else:
                r -= 1
        
        return res

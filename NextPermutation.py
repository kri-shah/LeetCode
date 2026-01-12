class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        piv = len(nums) - 2
        while piv >= 0 and nums[piv] >= nums[piv + 1]:
            piv -= 1
        
        if piv >= 0:
            r = len(nums) - 1
            while nums[piv] >= nums[r]:
                r -= 1
            
            nums[piv], nums[r] = nums[r], nums[piv]
        
        piv += 1
        r = len(nums) - 1
        while piv < r:
            nums[piv], nums[r] = nums[r], nums[piv]
            piv += 1
            r -= 1
        
        
        

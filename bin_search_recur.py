class Solution(object):
    def bin(self, nums, target, left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.bin(nums, target, mid + 1, right)
        else:  # target < nums[mid]
            return self.bin(nums, target, left, mid - 1)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bin(nums, target, 0, len(nums) - 1)

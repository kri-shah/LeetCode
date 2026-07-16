class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = sum(nums[::2])
        total_odd = sum(nums[1::2])

        left_even = left_odd = 0
        res = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                total_even -= num
            else:
                total_odd -= num

            if left_even + total_odd == left_odd + total_even:
                res += 1

            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num

        return res

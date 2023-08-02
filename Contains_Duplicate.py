class Solution(object):
    def containsDuplicate(self, nums):
        numset = set()
        for num in nums:
            if num in numset:
                return True
            numset.add(num)

        return False

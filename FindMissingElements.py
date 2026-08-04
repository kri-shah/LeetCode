class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi = min(nums)
        mx = max(nums)
        num_set = set(nums)
        
        res = []
        for num in range(mi + 1, mx):
            if num not in num_set:
                res.append(num)
        
        return res

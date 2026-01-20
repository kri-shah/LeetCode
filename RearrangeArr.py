class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        pre = [0]
        for num in nums:
           pre.append(num + pre[-1]) 
        
        
        res = 0
        for num in pre:
            if num > 0:
                res += 1
        
        return res

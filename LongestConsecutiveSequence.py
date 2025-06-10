class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)        
        starts = []
        for pos, i in enumerate(nums):            
            if i-1 not in numset:
                starts.append(i)
        
        maxcount = 0
        for s in starts:
            t = s
            count = 0
            while t in numset:
                t+=1
                count+=1
            maxcount = max(maxcount, count)

        return maxcount

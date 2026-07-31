class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = [0] * 100
        for num in nums:
            freq[num - 1] += 1

        res = 0
        for i in range(100):
            if freq[i] == 1:
                res += i + 1
        
        return res

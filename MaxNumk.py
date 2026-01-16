class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        
        res = 0
        for n in nums:
            if k - n in freq:
                res += 1
                freq[k - n] -= 1
                if freq[k - n] <= 0:
                    del freq[k - n]
            else:
                freq[n] += 1
        
        return res

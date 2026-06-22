class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)
        
        for c in text:
            if c in 'balloon':
                freq[c] += 1
        
        
        freq['o'] //= 2 
        freq['l'] //= 2 
        
        res = float('inf')
        for c in 'balloon':
            res = min(res, freq[c])
        
        return res

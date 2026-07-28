class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = defaultdict(int)
        mid = None
        
        for c in s:
            freq[c] += 1
        
        for key, val in freq.items():
            if val % 2 == 1:
                mid = key
                break

        res = []
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in freq:
                res.append(c * (freq[c] // 2))
        

        if mid:
            res = res + [mid] + res[::-1]
        else:
            res = res + res[::-1]
        
        return "".join(res)

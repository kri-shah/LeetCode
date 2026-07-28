class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        max_freq = max(freq.values())
        res = []
        
        for c in reversed(s):
            if freq[c] == max_freq:
                res.append(c)
            freq[c] -= 1

        return "".join(reversed(res))

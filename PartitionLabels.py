class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        res = []
        
        for c in s:
            freq[c] += 1
        
        start = 0
        chars = set()
        
        for i, c in enumerate(s):
            chars.add(c)
            freq[c] -= 1
            if freq[c] == 0:
                chars.remove(c)
                del freq[c]
                
                if not chars:
                    res.append(i - start + 1)
                    start = i + 1
        
        return res

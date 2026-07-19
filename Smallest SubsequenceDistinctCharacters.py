class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = dict()
        for i, c in enumerate(s):
            last[c] = i
        
        res = []
        used = set()
        for i, c in enumerate(s):
            if c not in used:
                while res and c <= res[-1] and last[res[-1]] > i:
                    used.remove(res.pop())
            
                res.append(c)
                used.add(c)
        
        return "".join(res)

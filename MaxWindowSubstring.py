class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freq_t = dict()
        for c in t:
            freq_t[c] = 1 + freq_t.get(c, 0)
        
        res = ""
        len_res = float('inf')
        
        freq_s = dict()
        l = 0
        need = len(freq_t)
        have = 0
        for r in range(len(s)):        
            freq_s[s[r]] = 1 + freq_s.get(s[r], 0)
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < len_res:
                    len_res = r-l+1
                    res = s[l:r+1]

                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        
        return res 
                    






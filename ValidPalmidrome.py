class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for c in s:
            if c.isalnum():
                string.append(c.lower())
        
        pal = "".join(string)

        l, r = 0, len(pal) - 1
        
        while l < r:
            if pal[l] != pal[r]:
                return False
            l += 1
            r -= 1
        
        return True

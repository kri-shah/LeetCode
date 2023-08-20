class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1 or len(s) == 0:
            return True
        pal = re.sub(r'\W+', '', s) 
        pal = pal.lower()
        
        pal = pal.replace('_', '') 
        n = len(pal)
        
        for x in range(1, n):
            print(pal[x])
            print(pal[n - x])
            if pal[x- 1] != pal[n - x]:
                return False
        return True

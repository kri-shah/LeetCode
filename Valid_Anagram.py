class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        str1 = s
        str2 = t

        str1 = list(str1)
        str2 = list(str2)
        str1.sort()
        str2.sort()
        print(str(str1) +" " + str(str2))
        for x in range(len(str1)):
            if str1[x] != str2[x]:
                return False
        
        return True
        

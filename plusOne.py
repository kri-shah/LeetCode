#beats Beats 80.64%of users with Python runtime
#beats Beats 90.64%of users with Python memory
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = ""
        for x in digits:
            temp += str(x)
        
        temp = int(temp) + 1

        ans = []
        for s in str(temp):
            ans.append(int(s))
        
        return ans

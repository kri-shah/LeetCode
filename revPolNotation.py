#Beats 99.23%of users with Python in runtime

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        opert = {'+':lambda x, y: x + y, '-':lambda x, y: x - y, '*':lambda x, y: x * y, 
            '/':lambda x, y: int(x / y)}
        
        stack = []
        ans = 0
        for x in tokens:
            if x not in opert:
                stack.append(x)
            elif stack:
                
                num1 = float(stack.pop())
                num2 = float(stack.pop())
                stack.append(opert[x] (num2, num1))
            
        return int(stack[-1])

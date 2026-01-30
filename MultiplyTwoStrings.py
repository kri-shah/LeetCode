class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        def add(n1, n2):
            if len(n1) < len(n2):
                n1 = '0' * (len(n2) - len(n1)) + n1
            if len(n2) < len(n1):
                n2 = '0' * (len(n1) - len(n2)) + n2
            
            carry = 0
            s = []
            for i in range(len(n2) - 1, -1, -1):
                dig_sum = int(n1[i]) + int(n2[i]) + carry
                s.append(str(dig_sum % 10))
                carry = dig_sum // 10
            
            if carry:
                s.append(str(carry))
            return "".join(reversed(s))    

        line = 0
        nums = []
        for i in range(len(num2) - 1, -1, -1):
            carry = 0
            prod = []
            for j in range(len(num1) - 1, -1, -1):
                digit = int(num1[j]) * int(num2[i]) + carry
                prod.append(str(digit % 10))
                carry = digit // 10
            
            if carry:
                prod.append(str(carry))
            
            prod.reverse()
            for i in range(line):
                prod.append('0')
            line += 1
            nums.append("".join(prod))
            if len(nums) == 2:
                nums.append(add(nums.pop(), nums.pop()))
        
        return nums[0]



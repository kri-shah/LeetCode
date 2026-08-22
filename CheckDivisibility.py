class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        loop_n = n
        
        while loop_n:
            digit = loop_n % 10
            digit_sum += digit
            digit_prod *= digit

            loop_n //= 10

        total = digit_sum + digit_prod
        
        if total == 0:
            return False
        
        return n % total == 0

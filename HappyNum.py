class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sum(num):
            res = 0
            while num:
                digit = num % 10
                num //= 10
                res += digit ** 2
            
            return res
        visited = set()
        while n not in visited:
            visited.add(n)
            
            n = digit_sum(n)
            print(n)
            if n == 1:
                return True
        
        return False

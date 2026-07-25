class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        second_largest = 0
        while n:
            digit = n % 10
            if digit > largest:
                largest, second_largest = digit, largest
            elif digit > second_largest:
                second_largest = digit

            n //= 10
        
        return largest * second_largest

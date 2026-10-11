import math
class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        primes = [True for i in range(n + 1)]
        primes[0] = False
        primes[1] = False
        
        for i in range(2, (math.floor(math.sqrt(n)) + 1)):
            if primes[i]:
                for j in range(i ** 2, n + 1, i):
                    primes[j] = False

        res = []
        count = 0
        for i in range(n + 1):
            if not primes[i]:
                continue
            count += i
            if count <= s:
                res.append(i)
            else:
                break
        
        return res

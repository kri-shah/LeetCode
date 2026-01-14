from collections import deque
from typing import List

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        def is_prime(n: int) -> bool:
            if n <= 1: return False
            if n <= 3: return True
            if n % 2 == 0 or n % 3 == 0: return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        max_q = deque() 
        min_q = deque()
        primes = deque()

        res = 0
        l = 0

        for r, val in enumerate(nums):
            if is_prime(val):
                while max_q and nums[max_q[-1]] <= val:
                    max_q.pop()
                max_q.append(r)

                while min_q and nums[min_q[-1]] >= val:
                    min_q.pop()
                min_q.append(r)

                primes.append(r)

            while primes and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q and max_q[0] == l:
                    max_q.popleft()
                if min_q and min_q[0] == l:
                    min_q.popleft()
                if primes and primes[0] == l:
                    primes.popleft()
                l += 1

            if len(primes) >= 2:
                second_last_prime = primes[-2]
                res += (second_last_prime - l + 1)

        return res

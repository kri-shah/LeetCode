class Solution:
    def minimumPushes(self, word: str) -> int:
        count = res = 0
        for i in range(len(word)):
            if i % 8 == 0:
                count += 1
            res += 1 * count
        
        return res

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        count = [0] * (n + 1)
        res = [0] * n
        
        for i, (a, b) in enumerate(zip(A, B)):
            count[a] += 1
            count[b] += 1
            res[i] = res[i - 1]
            
            if count[a] == 2:
                res[i] = 1 + res[i - 1]
            if count[b] == 2 and a != b:
                res[i] += 1 

        
        return res
            

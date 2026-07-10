class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        path = []
        def combo(i, s):
            if s == target:
                res.append(path[:])
                return
            
            if i == n or s > target:
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                combo(j + 1, s + candidates[j])
                path.pop()
        
        combo(0, 0)
        return res

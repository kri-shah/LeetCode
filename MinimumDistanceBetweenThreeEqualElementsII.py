class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indicies = defaultdict(list)
        res = float('inf')
        for i, num in enumerate(nums):
            indicies[num].append(i)
        
        for group in indicies.values():
            if len(group) <= 2:
                continue
            for i in range(len(group)):
                if i + 2 >= len(group):
                    break
                res = min(res, 2 * (group[i + 2] - group[i]))
        # | i - j | + | j - k | + k - i
        # - i + k + k - i
        # = 2k - 2i
        return res if res != float('inf') else -1

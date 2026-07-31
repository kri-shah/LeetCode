class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        window = set()
        l = 0
        res = float('inf')
        for i in range(len(cards)):
            while l < i and cards[i] in window:
                res = min(res, i - l + 1)
                window.remove(cards[l])
                l += 1
            window.add(cards[i])
        
        return res if res != float('inf') else -1

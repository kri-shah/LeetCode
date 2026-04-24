class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        free = left = right = 0
        for m in moves:
            if m == 'L':
                left += 1
            elif m == 'R':
                right += 1
            else:
                free += 1
        
        res = 0
        if left > right:
            res = left + free - right
        else:
            res = right + free - left
        
        return res

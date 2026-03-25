class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        res = 0
        while tx >= sx or ty >= sy:
            if tx == sx and ty == sy:
                return res
            res += 1
            
            if tx < ty or (tx == ty and sx > sy):
                tx, ty = ty, tx
                sx, sy = sy, sx

            if tx >= ty * 2:
                if tx % 2:
                    return -1
                tx //= 2
            else:
                tx -= ty
        
        return -1

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        ROWS = len(room)
        COLS = len(room[0])
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        r = c = d = 0
        seen = set()
        clean = set()
        while (r, c, d) not in seen:
            seen.add((r, c, d))
            clean.add((r, c))
            moved = False
            for _ in range(4):
                newr, newc = r + directions[d][0], c + directions[d][1]
                if 0 <= newr < ROWS and 0 <= newc < COLS and room[newr][newc] != 1:
                    r, c = newr, newc
                    moved = True
                    break
                d = (d + 1) % 4
            
            if not moved:
                break
        
        return len(clean)

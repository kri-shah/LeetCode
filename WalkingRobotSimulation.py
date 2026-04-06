class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 1
        posx, posy = 0, 0
        ans = 0
        obstacle_set = set()
        
        for obs in obstacles:
            obstacle_set.add(tuple(obs))

        for command in commands:
            if command == -2:
                x, y = -y, x
            elif command == -1:
                x, y = y, -x
            else:
                for _ in range(command):
                    nx, ny = posx + x, posy + y
                    if (nx, ny) in obstacle_set:
                        break
                    posx, posy = nx, ny
                    ans = max(ans, posx * posx + posy * posy)

        return ans

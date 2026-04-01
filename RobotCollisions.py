class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [(positions[i], healths[i], directions[i], i) 
        for i in range(len(positions))]
        
        robots.sort()

        stack = []
        for p, h, d, i in robots:
            stack.append([h, i, d])
            if d == 'L':
                while len(stack) >= 2 and (stack[-2][2] == 'R' 
                and stack[-1][2] == 'L'):
                    if stack[-1][0] == stack[-2][0]:
                        stack.pop()
                        stack.pop()
                    elif stack[-1][0] > stack[-2][0]:
                        left_health, left_idx, left_dir = stack.pop()
                        stack.pop()
                        stack.append([left_health - 1, left_idx, left_dir])
                    else:
                        stack.pop()
                        stack[-1][0] = stack[-1][0] - 1
        
        stack.sort(key = lambda x: x[1])
        return [health for health, _, _ in stack]

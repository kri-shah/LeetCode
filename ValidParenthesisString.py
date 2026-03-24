class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = deque()
        open_stack = []
        for i, c in enumerate(s):
            if c == '(':
                open_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        if len(open_stack) > len(star_stack):
            return False
        
        for char in open_stack:
            while star_stack and char > star_stack[0]:
                star_stack.popleft()
            
            if star_stack and char < star_stack[0]:
                star_stack.popleft()
            else:
                return False
            
        return True

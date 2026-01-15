class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        
        for i in range(1, len(s)):
            if stack:
                char_diff = abs(ord(stack[-1]) - ord(s[i]))
                if (char_diff == 1 or char_diff == 25): 
                    stack.pop()
                    continue
            
            stack.append(s[i])
        
        return "".join(stack)

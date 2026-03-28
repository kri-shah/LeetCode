class Solution:
    def expand(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):            
            if s[i] == "{":
                temp = []
                i += 1
                while s[i] != "}":
                    if s[i] != ',':
                        temp.append(s[i])
                    i += 1
                arr.append(temp)
            else:
                arr.append([s[i]])
            i += 1
        
        res = []

        def backtrack(path, i):
            if len(path) == len(arr):
                res.append("".join(path))
                return
            
            
            for char in arr[i]:
                path.append(char)
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        res.sort()
        return res

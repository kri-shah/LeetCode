class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:    
        n = len(arr)
        
        stack = [start]
        visited = set([start])
        
        while stack:
            indx = stack.pop()
            if arr[indx] == 0:
                return True
            
            new_plus = indx + arr[indx]
            if 0 <= new_plus < n and new_plus not in visited:
                stack.append(new_plus)
                visited.add(new_plus)
            
            new_minus = indx - arr[indx]
            if 0 <= new_minus < n and new_minus not in visited:
                stack.append(new_minus)
                visited.add(new_minus)
        
        return False

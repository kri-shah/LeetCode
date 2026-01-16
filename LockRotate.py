class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = {i for i in deadends}
        
        if '0000' in visited:
            return -1
        
        queue = deque()
        queue.append(([0, 0, 0 ,0], 0))
        
        res = float('inf')
        
        while queue:
            lock, turns = queue.popleft()
            str_lock = "".join(str(l) for l in lock)
            
            if str_lock == target:
                res = min(res, turns)
                continue

            turns += 1
            for i in range(4):
                start = lock[i]
                lock[i] = (start + 1) % 10
                if "".join(str(l) for l in lock) not in visited:
                    queue.append((lock[:], turns))
                    visited.add("".join(str(l) for l in lock))
                
                lock[i] = (start - 1) 
                
                if lock[i] < 0:
                    lock[i] = 9

                if "".join(str(l) for l in lock) not in visited:
                    queue.append((lock[:], turns))
                    visited.add("".join(str(l) for l in lock))
                
                lock[i] = start
        
        return res if res != float('inf') else -1

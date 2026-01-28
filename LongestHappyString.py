class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        
        heapq.heappush(heap, (a * -1, 'a'))
        heapq.heappush(heap, (b * -1, 'b'))
        heapq.heappush(heap, (c * -1, 'c'))
        
        res = []
        wait = deque()
        while heap:
            num, char = heapq.heappop(heap)
            
            if num >= 0:
                continue
            
            if len(res) >= 2 and res[-1] == res[-2] and res[-1] == char:
                wait.append((num, char))
                continue
            elif wait:
                heapq.heappush(heap, wait.popleft())
            
            res.append(char)
            heapq.heappush(heap, (num + 1, char))
        
        return "".join(res)


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] -= 1
        
        heap = []
        for char, count in freq.items():
            heapq.heappush(heap, (count, char))
        
        res = []
        while heap:
            count, char = heapq.heappop(heap)
        
            if res and char == res[-1]:
                if heap:
                    count2, char2 = heapq.heappop(heap)
                    res.append(char2)
                    if count2 + 1 < 0:
                        heapq.heappush(heap, (count2 + 1, char2))
                    heapq.heappush(heap, (count, char))
                else:
                    return ""
            else:
                res.append(char)
                if count + 1 < 0:
                    heapq.heappush(heap, (count + 1, char))
        
        return "".join(res)

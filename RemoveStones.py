class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapq.heapify(heap)
        for _ in range(k):
            stone = heapq.heappop(heap) * -1
            stone = stone - (stone//2)
            heapq.heappush(heap, -stone)
        
        return -sum(heap)

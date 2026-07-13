class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        
        res = [len(heights) - 1]
        max_h = heights[-1]
        
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_h:
                res.append(i)
            max_h = max(heights[i], max_h)
        
        return res[::-1]

#Beats 98.21%of users with Python in runtime

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            if height[l] <= height[r]:
                if height[l] * (r-l) > area:
                    area = height[l] * (r-l)
                l+=1

            elif height[l] > height[r]:
                if height[r] * (r-l) > area:
                    area = height[r] * (r-l) 
                r-=1
        
        return area

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        l = 0
        r = len(height) - 1
        while l < r:
            m = max(m, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
    
        return m
        

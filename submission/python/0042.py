class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        
        ans = 0
        max_left = [0 for _ in range(len(height))]
        max_right = [0 for _ in range(len(height))]
        
        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i-1])
        
        max_right[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
            
        for i in range(len(height)):
            ans += min(max_left[i], max_right[i]) - height[i]
            
        return ans

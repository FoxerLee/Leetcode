class Solution(object):
            
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = nums[0]
        
        if step == 0 and len(nums) > 1:
            return False
        
        for i in range(1, len(nums) - 1):
            step = max(step-1, nums[i])
            
            if (step == 0):
                return False
        
        return True
        
    
            
        

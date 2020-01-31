class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
                
        for i in range(n):
            a = abs(nums[i])
            
            nums[a-1] = - abs(nums[a-1])
            
        
        for i in range(n):
            if nums[i] > 0:
                return i+1
            
        return n+1
        

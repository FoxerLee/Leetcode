class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 1
        
        while i < len(nums):
            if nums[i-1] > nums[i]:
                return nums[i]
            i += 1
            
        return nums[0]

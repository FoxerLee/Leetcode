class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0        
        ans = float('inf')
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            while add >= s:
                ans = min(ans, i-left+1)
                add -= nums[left]
                left += 1
                
        # while add >= s and left < len(nums):
            
                
        return ans if ans != float('inf') else 0

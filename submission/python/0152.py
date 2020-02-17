class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = nums[0]
        imin = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp
                
            imax = max(imax*nums[i], nums[i])
            imin = min(imin*nums[i], nums[i])
            
            ans = max(ans, imax)
            
        return ans

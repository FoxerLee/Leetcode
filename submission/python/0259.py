class Solution:
        
    def two(self, nums, j, target):
        ans = 0
        l = j
        r = len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                ans += r - l
                l += 1
            else:
                r -= 1
        return ans
        
        
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans = 0
        nums = sorted(nums)
        for i in range(len(nums)-2):
            ans += self.two(nums, i+1, target-nums[i])
        
        return ans

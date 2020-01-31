class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0 for _ in range(len(nums))]
        ans = 1
        dp[0] = 1
        for i in range(1, len(nums)):
            tmp = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmp = max(tmp, dp[j])
                    
            dp[i] = tmp + 1
            ans = max(ans, dp[i])
                
        return ans

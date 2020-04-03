class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if nums == []:
            return 0
        
        _len = len(nums)
        
        dp = [collections.defaultdict(int) for _ in range(_len+1)]
        dp[0][0] = 1
        
        for i, num in enumerate(nums):
            for key, value in dp[i].items():
                dp[i+1][key+num] += value
                dp[i+1][key-num] += value
        
        return dp[_len][S]
                

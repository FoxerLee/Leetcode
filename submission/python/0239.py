class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        ans = []
        for i in range(len(nums)-k+1):
            tmp = nums[i:i+k]
            ans.append(max(tmp))
            
        return ans

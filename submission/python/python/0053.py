class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        curSum = maxSum = nums[0]
        for cur in nums[1:]:
            curSum = max(cur, curSum+cur)
            maxSum = max(maxSum, curSum)

        return maxSum
        
            

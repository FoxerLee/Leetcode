class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        pre_sum = {}
        curr_sum = 0
        flag = False
        pre_sum[0] = -1
        for i in range(len(nums)):
            curr_sum += nums[i]
            # remain = 0
            if k != 0:
                curr_sum = curr_sum % k
            if curr_sum in pre_sum:
                if i-pre_sum[curr_sum] > 1:
                    return True
            else:
                pre_sum[curr_sum] = i
                
        return False
            
            

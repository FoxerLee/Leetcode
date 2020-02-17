class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        cur = 0
        p2 = len(nums) - 1
        
        while cur <= p2:
            
            if nums[cur] == 0:
                tmp = nums[cur]
                nums[cur] = nums[p0]
                nums[p0] = tmp              
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                tmp = nums[cur]
                nums[cur] = nums[p2]
                nums[p2] = tmp
                # cur += 1
                p2 -= 1
            else:
                cur += 1
                
        # return nums

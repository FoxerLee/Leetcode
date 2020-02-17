class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        
        res = []
        
        length = len(nums)
        if length == 0 or nums[0]*4 > target or nums[length-1]*4 < target:
            return []
        
        for i in range(0, length-3):
            if nums[i] == nums[i-1] and i > 0:
                continue
            for j in range(i+1, length-2):
                left = j+1
                right = length-1
                while left < right:
                    
                    if nums[i]+nums[j]+nums[left]+nums[right] == target:
                        res.append(tuple([nums[i], nums[j], nums[left], nums[right]]))
                        left += 1
                        right -= 1
                    elif nums[i]+nums[j]+nums[left]+nums[right] < target:
                        left += 1
                    else:
                        right -= 1
                        
                        
        return set(res)

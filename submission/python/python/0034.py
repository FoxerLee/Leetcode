class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        le = self.find_index(nums, target, True)

        if le == len(nums) or nums[le] != target:
            return [-1, -1]

        return [le, self.find_index(nums, target, False)-1]
    
    def find_index(self, nums, target, if_left):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target or (if_left and nums[mid] == target):
                right = mid
            else:
                left = mid + 1

        return left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index,item in enumerate(nums):
            if item >= target:
                return index
        return len(nums)

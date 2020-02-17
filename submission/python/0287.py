class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[nums[0]]]
        slow = nums[nums[0]]
        
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
        slow2 = nums[0]
        
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
            
        return slow2

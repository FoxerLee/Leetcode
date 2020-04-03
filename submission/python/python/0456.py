class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins = []
        min_num = float('inf')
        for num in nums:
            min_num = min(min_num, num)
            mins.append(min_num)
            
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > mins[i]:
                while stack != [] and stack[-1] <= mins[i]:
                    stack.pop()
                if stack != [] and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
                
        return False
                    

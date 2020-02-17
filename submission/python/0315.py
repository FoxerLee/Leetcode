class Solution:
    # def rec(self, num, nums):
        
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        
        sorted_nums = []
        for i in range(len(nums)-1, -1, -1):
            # tmp = sorted(nums[i+1:])
            bisect.insort(sorted_nums, nums[i])
            ans.append(bisect.bisect_left(sorted_nums, nums[i]))
            
        ans.reverse()  
        return ans
            

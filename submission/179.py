import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if x+y < y+x:
                return 1
            if x+y > y+x:
                return -1
            return 0
        
        nums = map(str, nums)
        nums = sorted(nums, key=functools.cmp_to_key(cmp))
        
        largest_num = "".join(nums)
        
        return largest_num if largest_num[0] != '0' else '0'
        
        

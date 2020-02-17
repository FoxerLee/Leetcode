class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict.pop(num)
                
        return dict.popitem()[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         dict = {}
        
#         for num in nums:
#             if num not in dict:
#                 dict[num] = 1

#             elif dict[num] == 2:
#                 dict.pop(num)

#             else:
#                 dict[num] += 1
                
#         return dict.popitem()[0]
        return int((3*sum(set(nums)) - sum(nums))/2)

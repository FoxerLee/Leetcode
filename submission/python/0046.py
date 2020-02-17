class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            if len(nums) == 0:
                return [[]]

            res = []
            for i in range(len(nums)):
                for l in self.permute(nums[0:i] + nums[i + 1:]):
                    res.append([nums[i]] + l)

            return res
        

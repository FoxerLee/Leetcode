class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        res = []
        for i in range(len(nums)):
            for l in self.permuteUnique(nums[0:i] + nums[i + 1:]):
                tmp = [nums[i]] + l
                if tmp not in res:
                    res.append([nums[i]] + l)
                    
        # res = list(set(res))
        
        return res

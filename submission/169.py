class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        for num, fre in counter.items():
            if fre > len(nums)/2:
                return num

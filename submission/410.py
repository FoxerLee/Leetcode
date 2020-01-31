class Solution:
    def check(self, nums, m, sum):
        split_c = 1
        curr = 0
        
        for num in nums:
            curr += num
            if curr > sum:
                curr = num
                split_c += 1          
                
        if split_c > m:
            return False
        else:
            return True
    
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)
        
        while l < r:
            mid = l+(r-l)//2
            if self.check(nums, m, mid):
                r = mid
            else:
                l = mid+1
        return r

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, 0
        ans = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                k -= 1
                p2 = 0
            while k == 0:
                if nums[p1] % 2 == 1:
                    k += 1
                p2 += 1
                p1 += 1
            ans += p2
            
        return ans
            

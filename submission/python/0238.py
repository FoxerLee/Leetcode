class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]
        L = [1 for _ in range(len(nums))]
        R = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            L[i] = L[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            R[i] = R[i+1]*nums[i+1]
            
        for i in range(len(nums)):
            ans[i] = L[i]*R[i]
            
        return ans

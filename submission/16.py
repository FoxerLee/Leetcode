class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        sum = 100000
        # closet = 0

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if abs(tmp-target) < abs(sum-target):
                    sum = tmp
                    # closet = abs(tmp-target)

                if tmp == target:
                    return tmp

                if tmp - target < 0:
                    l += 1
                elif tmp - target > 0:
                    r -= 1

        return sum

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        # i = 1
        # while (i < len(nums)-1):
        #     tmp = nums[i]
        #     nums[i] = nums[i+1]
        #     nums[i+1] = tmp
        #     i += 2
        
        is_up = True
        for i in range(len(nums)-1):
            if is_up:
                if nums[i] > nums[i+1]:
                    tmp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = tmp
            else:
                if nums[i] < nums[i+1]:
                    tmp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = tmp
            is_up = False if is_up == True else True
            

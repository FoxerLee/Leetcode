class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        # tmp = nums[:]
        
        first_de = -1
        for i in range(n, 0, -1):
            if nums[i-1] < nums[i]:
                first_de = i-1
                break
        
        larger = len(nums) - 1
        if first_de >= 0:
            for j in range(n, first_de, -1):
                if nums[j] > nums[first_de]:
                    larger = j
                    break
        
        tmp = nums[first_de]
        nums[first_de] = nums[larger]
        nums[larger] = tmp

        # nums = nums[:first_de] + sorted(nums[first_de+1:n])
        i = first_de + 1
        j = n

        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

            i += 1
            j -= 1
        
                
        
            

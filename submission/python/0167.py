class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1
        
        while p1 < len(numbers):
            add_sum = numbers[p1] + numbers[p2]
            if add_sum == target:
                return [p1+1, p2+1]
            
            elif add_sum > target:
                p2 -= 1
            else:
                p1 += 1
                
        return [-1, -1]

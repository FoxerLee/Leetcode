class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = collections.defaultdict(int)
        
        for num in nums:
            if num in hash_table.keys():
                return True
            hash_table[num] = 1
            
        return False

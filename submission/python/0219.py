class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = collections.defaultdict(int)
        
        for i, num in enumerate(nums):
            if num in hash_table.keys():
                return True
            
            hash_table[num] += 1
            
            if len(hash_table) > k:
                hash_table.pop(nums[i-k])
                
        return False
                

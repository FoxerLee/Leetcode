class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = collections.defaultdict(int, {0:1})
        
        ans = 0
        sum = 0
        for n in nums:
            sum += n
            ans += hash_map[sum-k]
            hash_map[sum] += 1
        
                

        return ans

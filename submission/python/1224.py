class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        freq = collections.defaultdict(int)
        ans = 0
        max_f = 0
        
        for i in range(len(nums)):
            count[nums[i]] += 1
            freq[count[nums[i]]-1] -= 1
            freq[count[nums[i]]] += 1
            
            max_f = max(max_f, count[nums[i]])
            if max_f == 1 or max_f*freq[max_f] == i or ((max_f-1)*freq[max_f-1] + max_f-1) == i:
                ans = 1 + i
                
        return ans

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fre_dict = collections.defaultdict(list)
        for i in range(len(nums)):
            fre_dict[nums[i]].append(i)
            
        sorted_dict = sorted(fre_dict.values(), key = lambda x:len(x))
        
        # sorted_idx = sorted(sorted_dict[0])
        sorted_idx = []
        length = len(sorted_dict[-1])
        for all_idx in sorted_dict:
            if len(all_idx) == length:
                sorted_idx.append(all_idx)
        
        ans = float('inf')
        
        for all_idx in sorted_idx:
            tmp = sorted(all_idx)
            if (tmp[-1] - tmp[0] + 1) < ans:
                ans = tmp[-1] - tmp[0] + 1
        
        return ans

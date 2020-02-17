class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_dict = collections.defaultdict(int)
        
        for num in nums:
            fre_dict[num] += 1
        
        
            
        return heapq.nlargest(k, fre_dict.keys(), key=fre_dict.get) 

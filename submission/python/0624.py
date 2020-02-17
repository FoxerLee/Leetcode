class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_v = arrays[0][0]
        max_v = arrays[0][-1]
        for i in range(1, len(arrays)):
            res = max(max(max_v - arrays[i][0], arrays[i][-1] - min_v), res)
            max_v = max(max_v, arrays[i][-1])
            min_v = min(min_v, arrays[i][0])
            
            
        
        return res

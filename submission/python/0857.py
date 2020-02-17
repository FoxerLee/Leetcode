from heapq import *
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        pairs = sorted([float(w/q), q] for q, w in zip(quality, wage))
        
        ans, q_sum = float('inf'), 0
        heap = []
        for pair in pairs:
            r, q = pair
            heappush(heap, -q)
            
            q_sum += q
            if len(heap) > K:
                q_sum += heappop(heap)
            
            if len(heap) == K:
                ans = min(ans, q_sum*r)
                
        return ans

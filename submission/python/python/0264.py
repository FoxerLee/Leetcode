class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = []
        heap = [1]
        
        while len(ans) < n:
            _min = heapq.heappop(heap)
            ans.append(_min)
            for i in [2,3,5]:
                if _min*i not in heap:
                    heapq.heappush(heap, _min*i)
            
        return ans[-1]

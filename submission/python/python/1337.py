import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i, row in enumerate(mat):
            heapq.heappush(rows, (sum(row), i))
            
        ans = []
        for _ in range(k):
            row_i = heapq.heappop(rows)[1]
            ans.append(row_i)
            
        return ans

        
            

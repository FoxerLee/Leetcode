import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans = []
        seen = set()
        seen.add(1)
        heap = []
        heapq.heappush(heap, 1)
        while len(ans) < n:
            cur = heapq.heappop(heap)
            ans.append(cur)
            for prime in primes:
                new = cur*prime
                if new not in seen:
                    heapq.heappush(heap, new)
                    seen.add(new)
                
        
        return ans[-1]

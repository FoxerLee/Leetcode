import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        hash_ = collections.defaultdict(int)
        for char in s:
            hash_[ord(char)] += 1
            
        heap = []
        for key, val in hash_.items():
            heapq.heappush(heap, (val*(-1), key))
            
        ans = ""
        while heap:
            counts, char = heapq.heappop(heap)
            counts = counts*(-1)
            char = chr(char)
            ans = ans + "".join([char for _ in range(counts)])
            
        return ans

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        pairs = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(pairs, (num1+num2, [num1, num2]))
                
        ans = []
        for _ in range(k):
            if pairs:
                _, pair = heapq.heappop(pairs)
                ans.append(pair)
        
        return ans
        

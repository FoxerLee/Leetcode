class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        _sum = sum(arr[:k])
        if _sum/k >= threshold:
            ans += 1
        
        for i in range(k, len(arr)):
            _sum = _sum - arr[i-k] + arr[i]
            if _sum/k >= threshold:
                ans += 1
        
        return ans

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        l = 0
        r = len(citations) - 1
        while l <= r:
            mid = l + (r-l) // 2
            
            if len(citations) - mid == citations[mid]:
                return len(citations) - mid
            elif len(citations) - mid > citations[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return len(citations) - l

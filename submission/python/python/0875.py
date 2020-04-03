class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        l = 1
        r = max(piles)
        
        while l < r:
            mid = int((l+r) / 2)
            if not sum(int((p-1)/mid) + 1 for p in piles) <= H:
                l = mid + 1
            else:
                r = mid
                
        return l
            

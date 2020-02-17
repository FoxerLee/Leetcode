class Solution:
    def helper(self, houses, heaters, radius):
        tmp = 0
        
        for h in heaters:
            lb = h - radius
            rb = h + radius
            while tmp < len(houses) and lb <= houses[tmp] <= rb:
                tmp += 1
                
            if tmp == len(houses):
                return True
        
        return False
        
        
        
    
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        
        l = 0
        r = max(max(houses), max(heaters))
        
        while l < r:
            mid = int((l+r)/2)
            if self.helper(houses, heaters, mid):
                r = mid
            else:
                l = mid + 1
                
        return l
            
        
        

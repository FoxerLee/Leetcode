class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        min = 100000000
        
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            
            if prices[i] - min > res:
                res = prices[i] - min
                
        return res
        

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {"R": 0, "L": 0}
        ans = 0
        for c in s:
            d[c] += 1
            if d["R"] == d["L"] and d["R"] + d["L"] != 0:
                ans += 1
        
        return ans
                
            

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(list(J))
        
        ans = 0
        for s in S:
            if s in J:
                ans += 1
                
        return ans

class Solution:
    def confusingNumberII(self, N: int) -> int:
        
        valid = [0,1,6,8,9]
        mapping = {0: 0,1: 1,6: 9,8: 8, 9: 6}
        self.count = 0
        def backtrack(v, rotation,digit):
            self.count += v != rotation
            for i in valid: 
                if v*10+i <= N:
                    backtrack(v*10+i, mapping[i]*digit + rotation, digit*10)
        if N >= 1: backtrack(1,1, 10)
        if N >= 6: backtrack(6,9,10)
        if N >= 8: backtrack(8,8,10)
        if N >= 9: backtrack(9,6,10)
        
        return self.count 

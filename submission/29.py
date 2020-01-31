class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        abs_end = abs(dividend)
        abs_sor = abs(divisor)
        
        while abs_sor <= abs_end:
            ans_once = 1
            temp = abs_sor
            while temp*2 <= abs_end:
                ans_once *= 2
                temp *= 2
            abs_end = abs_end - temp
            ans += ans_once
            
        
        
#         while abs_sor <= abs_end:
#             ans += 1
#             abs_end -= abs_sor
        
        if divisor*dividend < 0:
            return max(-2147483648, -ans)
        else:
            return min(2147483647, ans)


        

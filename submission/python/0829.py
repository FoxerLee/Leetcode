class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        
        k = 1
        while k*(k+1) <= N*2:
            if 2*N % k == 0:
                y = 2 * N / k - k - 1
                if y % 2 == 0 and y >= 0:
                    ans += 1
            k+=1
                    
        return ans

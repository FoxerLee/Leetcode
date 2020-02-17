class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == 0:
            return 1
        
        elif n < 0:
             return 1/self.myPow(x, -n)
            
        elif n % 2 == 0:
            y = self.myPow(x, n//2)
            return y*y
        else:
            y = self.myPow(x, (n-1)//2)
            return x*y*y
        
        

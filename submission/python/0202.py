class Solution:
    def get_sum(self, n):
        str_n = str(n)
        
        num_sum = 0
        for num in str_n:
            num_sum += int(num)**2
        
        return num_sum
    
    def isHappy(self, n: int) -> bool:
        
        slow = n
        fast = self.get_sum(n)
        
        while fast != 1 and slow != fast:
            slow = self.get_sum(slow)
            fast = self.get_sum(self.get_sum(fast))
            
        return fast == 1
        
        

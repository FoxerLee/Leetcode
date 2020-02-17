class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
            
        sorted_A = sorted(A)
        
        p1 = 0
        p2 = len(sorted_A) - 1
        
        max_sum = -1
        
        
        
        while p1 < p2:
            if sorted_A[p1] + sorted_A[p2] >= K:
                p2 -= 1
                
            else:
                if sorted_A[p1] + sorted_A[p2] > max_sum:
                    max_sum = sorted_A[p1] + sorted_A[p2]
                p1 += 1
                    
        return max_sum
            
            
            
            

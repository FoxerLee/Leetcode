class Solution:
    def check(self, x, A, B):
        ra = rb = 0
        for i in range(len(A)):
            if A[i] != x and B[i] != x:
                return -1
            elif A[i] != x:
                ra += 1
            elif B[i] != x:
                rb += 1
        return min(ra, rb)
    
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ra = self.check(A[0], A, B)
        rb = self.check(B[0], A, B)
        
        if ra == -1 and rb == -1:
            return -1
        elif ra == -1 and rb != -1:
            return rb
        elif ra != -1 and rb == -1:
            return ra
        elif ra != -1 and rb != -1:
            return min(ra, rb)

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        a = (C-A)*(D-B)
        b = (G-E)*(H-F)
        
        interact = max(0, min(D, H)-max(B, F))*max(0, min(C, G)-max(A, E))
        
        return a + b - interact

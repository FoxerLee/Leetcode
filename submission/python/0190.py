class Solution:
    def reverseBits(self, n: int) -> int:   
        bits = bin(n)[2:]
        bits = "".join(["0" for _ in range(32-len(bits))]) + bits
        return int(bits[::-1], 2)
        
        

class Solution:
    def findComplement(self, num: int) -> int:
        num_2 = str(bin(num))[2:]
        
        com = ""
        for c in num_2:
            if c == '1':
                com += '0'
            else:
                com += '1'
                
        res = int(com, 2)
        
        return res
